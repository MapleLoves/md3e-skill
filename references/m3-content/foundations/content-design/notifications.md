---
source: https://m3.material.io/foundations/content-design/notifications
title: "Notifications"
captured: 2026-09-14
---

# Notifications

> Notifications help people see information they need or want at the right time

Notifications should:

-   Be about the user, not the product
-   Be precise, timely, actionable, contextual, and relevant
-   Give users easy controls to opt out
-   Not be used to send unsolicited ads

![](../../_assets/lw53k6lt-1-fc3c24363406ef0d2e34.png)

### Put important information at the top

Put the most important info at the beginning and make it easy to understand. People skim rather than read, often in an F shape. When it makes sense, try to move the most critical information to the front of sentences, rather than the end, where it may get overlooked or truncated.

![Three notifications from Google apps that include the point of the notification in the header.](../../_assets/lw53kfhk-2-f8defb8b824d9aa39e57.png)

check Do

Prioritize the most important information

![Three notifications from Google apps that include app names repeated in the header, instead of important information.](../../_assets/lw53kk0k-3-b08ea66991476cfc687f.png)

close Don’t

Don't waste characters on app names, niceties, or unimportant information

### Tell users what they can do

If you’re prompting someone to take action, make that clear. CTAs should be concise, specific, and actionable. If you know what motivates people to take action, add it. 

![Two notifications from Google maps that include actionable information in the header.](../../_assets/lw53kq5j-4-00e6771765bf08a8b7bf.png)

check Do

Clearly guide the user to their next action

![Two notifications from Google apps with non-actionable headers.](../../_assets/lw53kvqx-5-11464b2bff498ee231df.png)

close Don’t

Don't bury next steps

### Make it relevant and personal

A notification shouldn’t be sent to everyone. The more you broaden the audience and the message for a notification, the more you risk being irrelevant. Consider user segments, in-app behavior, and personalized information to make sure notifications go to people who will benefit most from them.

![A Google maps notification in Memphis, TN that’s personalized to the user’s location downtown.](../../_assets/lw53l2ot-6-612db39d4adfa11a698d.png)

check Do

Be specific to capture user attention

![A Google maps notification in Memphis, TN that’s generic to the city, rather than the area.](../../_assets/lw53l86v-7-4c35b04398ad3b70eaa6.png)

close Don’t

Don’t be so generic as to lose value

### Avoid dynamic text

Dynamic text are words that are implemented by engineering to change based on the user or context, like adding a user’s campaign name to headline or “good afternoon” when users log in at certain times.

Try not to use dynamic text in notifications. It often breaks character limits, especially in headlines when translated. Text that gets truncated in the headline will not expand, even in expandable notifications. If you must use dynamic text in the headline, try to pair it with no more than one additional word. Create a backup notification that fits the character count when your primary notification won’t. 

![Two notifications, one with dynamic text in the body, and the other with dynamic text in the header that’s formatted to always be short.](../../_assets/lw53lep9-8-51575623c392f3a4b907.png)

check Do

Place dynamic text in the notification body, where there is more space. If you place dynamic text in the title, keep it very short.

![Two notifications with dynamic text in the header that’s too long and truncates.](../../_assets/lw53lk9g-9-79d7486ea6150c23c8af.png)

close Don’t

Don’t place dynamic text in a long notification title

### Mind your characters

Stay within these suggested character counts so text doesn’t get cut off:

-   Title: <29 chars
-   Collapsed body: <40 chars
-   Expanded  body: <80 chars; start with collapsed body and add to it
-   Button: 1-2 buttons (1-2 words each)

There’s more room for text on later versions of Android, but these limits are still recommended to prevent truncation on smaller devices.

![A short, relevant, and informative notification.](../../_assets/lw53ls3l-10-1b81d8f15a2aceb9ff66.png)

check Do

Keep notifications short and information-dense

### SMS messages

SMS helps users get messages when they might not have access to their Google Account. It’s used for important or urgent communication only. 

SMS breaks into multiple messages after a certain number of characters, resulting in increased costs. To avoid this, stick to the following character limits:

-   Latin languages:  <160 characters
-   Non-latin languages: <134 characters

If translation is needed, let translators know about the character limits in the message description. 

![An SMS notification that’s brief and truncates sensitive information.](../../_assets/lw53lzfr-11-60ea5a2792ac43af6d7c.png)

check Do

SMS messages should be brief and important

![An SMS notification that’s too long with too many links.](../../_assets/lw53m528-12-a51b9e71c18617c3432a.png)

close Don’t

Don’t use full emails or website links for text length

### Emoji with caution

Use emoji sparingly. Many don’t translate and aren’t universally understood across cultures. Experiments show that face and hand gesture emoji perform better than generic emoji because they tell a better story. Emoji should enhance content, not replace it.

Since it’s not clear to users whether emoji mean we’re sympathizing with them or attempting to project our feelings onto them, don’t use emoji to accentuate bad news. In experiments, there was a strong negative reaction to negative emoji, such as frowning face, anguished face, and weary face.

Gen Z adds another cultural nuance to emoji by [inventing new meanings](https://www.textnow.com/blog/the-next-generation-of-emojis-gen-z-explained/) that go beyond the official or literal [definitions](https://emojipedia.org/).

![A notification about coffee with a coffee emoji at the end of the header.](../../_assets/lw53mcby-13-d68b4b65c191751f77c0.png)

check Do

Use emoji only to enhance a message

![A notification about high traffic volume on a route to work that uses upset emoji. A notification about coffee that substitutes a coffee emoji for the word “coffee.”](../../_assets/lw53mhmr-14-c18301710107cbd38697.png)

close Don’t

Don’t add negative emotions to a message. Don’t replace words with emoji.

### Don’t overdo delight

What seems funny or cute may not come across that way. When vying for limited user attention, be useful. Don’t focus on delight: delicately added and tested polish can better support Google’s brand.

![A notification that’s short and effective](../../_assets/lw53mqhm-15-90f345221681164b2b6e.png)

check Do

Prioritize straightforward and useful messages

![A notification that’s meant to be funny, but comes across as creepy where the application calls the user “human.”](../../_assets/lw53mx58-16-56cc6c5c2310d8ea5396.png)

close Don’t

Jokes aren’t appropriate for notifications

### Be day-specific

Use the days of the week. Don’t use “today,” “tomorrow,” “tonight,” or similar words. About 20% of users don’t see notifications on the day they’re sent, so “tomorrow” might be read when it’s “today” for the user.

An exception is when a notification auto-dismisses at a specific timestamp.

![](../../_assets/lw53n553-17-139bc196aa19aa793824.png)

check Do

Specify the day of the week so that it makes sense if someone reads it the following day

![](../../_assets/lw53nb80-18-333e7a7933948d28c5b0.png)

close Don’t

Don’t use relative terms like “today” or “tomorrow”

### Don’t interrupt the flow

If you have notifications or emails related to the onboarding process, make sure they don’t trigger during onboarding.

![](../../_assets/lw53nkf2-19-0cf58d7c294a43a7eac0.png)

close Don’t

Don't prompt the user with a notification or email that might interrupt an important moment

### Don’t name the product (again)

An app’s name or logo is already included in a notification’s design. Use the limited space for other information.

![](../../_assets/lw53ntem-20-1d9da28afd68605caad7.png)

check Do

Use the available space for useful information

![](../../_assets/lw53nz6w-21-d18f55a72f5cc7f400d3.png)

close Don’t

Don’t waste space repeating information that is already included by the OS

### Opting in and out

Give users a way to opt-out of notifications in context. If you don’t, they’ll have to dig into settings and may get frustrated. If you do offer opt-outs or opt-ins, make it clear what benefit the user is getting or losing.

![](../../_assets/lw53o6jr-22-0d8d84dd5cd3567b8fa9.png)

check Do

Make it easy for users to start or stop receiving notifications
