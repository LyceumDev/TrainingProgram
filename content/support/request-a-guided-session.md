---
title: Request a guided first session
section: support
order: 1
summary: One real task, one hour, a guide beside you and the assistant. The aim is finished work and a record you can resume from.
---
## What it is

A program guide sits with you and the assistant for about an hour, on one real task you are permitted to work on. The guide handles the setup, watches how the portal and the assistant work for you, and aims to have you leave with something finished. It is the recommended start for everyone, and the most reliable one.

## What to bring

- **One task** that took time but not judgment recently: a summary, a comparison, a first draft, a problem to state. If you are not sure, bring two and the guide will pick.
- **The sources** it rests on, with any real personal, customer, or payroll details replaced by placeholders and reference numbers.
- **Nothing else.** No preparation, no reading required. The lessons help but are not a prerequisite.

## What the session aims to leave you with

- A useful piece of work, verified, that you can actually use.
- A project record you can resume from tomorrow.
- A task guide, or an improvement to one, drawn from your task.
- A clear next step, including which environment fits your work.

## Request a session

This prototype has no server. Submitting hands the request to your email application, addressed to the program guide, with your answers written out; nothing is stored here. If the address is not configured yet, or your email application does not open, copy the summary that appears and send it yourself.

<form id="guided-session-form" class="form" data-to="" novalidate>
  <div class="field">
    <label for="req-name">Your name</label>
    <input id="req-name" name="name" type="text" required maxlength="120" autocomplete="name" aria-describedby="req-name-error">
    <p class="error" id="req-name-error" hidden>Please add your name so the guide knows who to reply to.</p>
  </div>
  <div class="field">
    <label for="req-role">Team or role</label>
    <input id="req-role" name="role" type="text" maxlength="120" autocomplete="organization-title">
  </div>
  <div class="field">
    <label for="req-work">The work you want to bring</label>
    <p class="hint" id="req-work-hint">One or two sentences describing the kind of task.</p>
    <p class="form-warning" id="req-work-warning">Reminder: remove customer, employee, payroll, credential, and other restricted details before sending.</p>
    <textarea id="req-work" name="work" required maxlength="600" aria-describedby="req-work-hint req-work-warning req-work-error"></textarea>
    <p class="error" id="req-work-error" hidden>Please describe the task in a sentence or two.</p>
  </div>
  <fieldset class="fieldset">
    <legend>Where will the assistant work?</legend>
    <div class="choices">
      <label><input type="radio" name="environment" value="I don't know yet — help me choose" checked> I don't know yet. Help me choose. <em>(the most common answer)</em></label>
      <label><input type="radio" name="environment" value="Browser and approved business applications"> Browser and approved business applications</label>
      <label><input type="radio" name="environment" value="Repository and development workspace"> Repository and development workspace</label>
      <label><input type="radio" name="environment" value="Specialized operational environment"> Specialized operational environment</label>
    </div>
  </fieldset>
  <div class="field">
    <label for="req-when">Good times for you</label>
    <input id="req-when" name="when" type="text" maxlength="200" placeholder="e.g. Tuesday or Thursday afternoons">
  </div>
  <div class="field">
    <label for="req-notes">Anything else</label>
    <p class="form-warning" id="req-notes-warning">Reminder: no restricted details here either.</p>
    <textarea id="req-notes" name="notes" maxlength="600" aria-describedby="req-notes-warning"></textarea>
  </div>
  <div class="field">
    <p class="form-warning">Before you send: check that nothing above names a real customer or employee, quotes real pay data, or contains a credential.</p>
    <button type="submit" class="btn btn-primary">Send the request</button>
  </div>
  <p id="form-status" class="form-status" role="status" tabindex="-1" hidden></p>
  <pre id="form-summary" hidden></pre>
</form>

## What happens next

The guide replies to agree a time. If you asked for help choosing an environment, the reply comes with three short questions: what work, which systems, what kind of data. That is the whole process.
