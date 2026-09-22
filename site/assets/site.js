/* AI Collaboration Portal — progressive enhancement only.
   Everything works without this file. It adds: the theme control (light is the
   default; a choice is remembered locally), the collapsed mobile menu, the recipe
   filters, and the guided-session request handoff. No analytics, no tracking. */
(function () {
  "use strict";
  var root = document.documentElement;

  // Theme control: a toggle button with a constant name and a pressed state.
  var themeToggle = document.querySelector(".theme-toggle");
  function applyTheme(theme, remember) {
    var dark = theme === "dark";
    if (dark) root.setAttribute("data-theme", "dark"); else root.removeAttribute("data-theme");
    if (themeToggle) themeToggle.setAttribute("aria-pressed", dark ? "true" : "false");
    if (remember) { try { localStorage.setItem("portal-theme", dark ? "dark" : "light"); } catch (e) { /* storage unavailable: the choice lasts for this page */ } }
  }
  applyTheme(root.getAttribute("data-theme") === "dark" ? "dark" : "light", false);
  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      applyTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark", true);
    });
  }

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Recipe filters and search
  var grid = document.getElementById("recipe-grid");
  if (grid) {
    var cards = Array.prototype.slice.call(grid.querySelectorAll(".card-recipe"));
    var empty = document.getElementById("recipe-empty");
    var search = document.getElementById("recipe-search");
    var state = { case: "", risk: "", q: "" };
    var apply = function () {
      var shown = 0;
      cards.forEach(function (c) {
        var ok = (!state.case || c.dataset.case === state.case) &&
                 (!state.risk || c.dataset.risk === state.risk) &&
                 (!state.q || c.textContent.toLowerCase().indexOf(state.q) !== -1);
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
      var live = document.getElementById("recipe-live");
      if (!live) {
        live = document.createElement("p");
        live.id = "recipe-live";
        live.className = "visually-hidden";
        live.setAttribute("aria-live", "polite");
        grid.parentNode.insertBefore(live, grid);
      }
      live.textContent = shown + (shown === 1 ? " recipe shown" : " recipes shown");
    };
    document.querySelectorAll(".chips").forEach(function (group) {
      var key = group.dataset.filter;
      group.querySelectorAll(".chip").forEach(function (chip) {
        chip.setAttribute("aria-pressed", chip.classList.contains("is-on") ? "true" : "false");
        chip.addEventListener("click", function () {
          group.querySelectorAll(".chip").forEach(function (c) { c.classList.remove("is-on"); c.setAttribute("aria-pressed", "false"); });
          chip.classList.add("is-on");
          chip.setAttribute("aria-pressed", "true");
          state[key] = chip.dataset.value;
          apply();
        });
      });
    });
    if (search) {
      search.addEventListener("input", function () { state.q = search.value.trim().toLowerCase(); apply(); });
    }
    var params = new URLSearchParams(location.search);
    var pre = params.get("case");
    if (pre) {
      var chip = document.querySelector('.chips[data-filter="case"] .chip[data-value="' + pre + '"]');
      if (chip) chip.click();
    }
  }

  // Guided first session request. The prototype has no server: the request is
  // handed to the person's email application, addressed to the configured
  // program address. Until that address is configured, the summary is shown
  // for the person to send themselves; nothing is silently lost.
  var form = document.getElementById("guided-session-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var invalid = false;
      form.querySelectorAll("[required]").forEach(function (f) {
        var err = document.getElementById(f.id + "-error");
        var bad = !f.value.trim();
        f.setAttribute("aria-invalid", bad ? "true" : "false");
        if (err) err.hidden = !bad;
        if (bad && !invalid) { f.focus(); invalid = true; }
      });
      if (invalid) return;
      var get = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ""; };
      var env = form.querySelector('input[name="environment"]:checked');
      var lines = [
        "Guided first session request",
        "",
        "Name: " + get("req-name"),
        "Team or role: " + get("req-role"),
        "The work I want to bring: " + get("req-work"),
        "Environment: " + (env ? env.value : "I don't know yet"),
        "Good times: " + get("req-when"),
        "",
        "Anything else: " + get("req-notes"),
        "",
        "Reminder: remove customer, employee, payroll, credential, and other restricted details before sending."
      ];
      var to = (form.dataset.to || "").trim();
      var summary = lines.join("\n");
      var status = document.getElementById("form-status");
      var pre = document.getElementById("form-summary");
      if (pre) { pre.hidden = false; pre.textContent = summary; }
      if (status) {
        status.hidden = false;
        status.textContent = to
          ? "Your email application should open with the request written for you, addressed to the program guide. If it does not, copy the summary below and send it yourself."
          : "The program's request address is not configured in this prototype yet. Copy the summary below and send it to your program guide.";
        status.focus();
      }
      if (to) {
        var href = "mailto:" + to + "?subject=" + encodeURIComponent("Guided first session request: " + get("req-name")) +
                   "&body=" + encodeURIComponent(summary);
        window.location.href = href;
      }
    });
  }
})();
