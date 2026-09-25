---
source: https://m3.material.io/components/cards/guidelines
title: "Cards"
captured: 2026-09-14
---

# Cards

> Cards display content and actions about a single subject

![3 variants of cards: elevated, filled, and outlined.](../../_assets/lwujy207-1-6eeeabdc42f0846d768d.png)

## Usage

Use a card to display content and actions on a single topic.

Cards should be easy to scan for relevant and actionable information. 

Elements like text and images should be placed on cards in a way that clearly indicates hierarchy.

![Example card containing an image, title, text, and button.](../../_assets/lwujyk5p-2-b043cd55ce2efe62517a.png)

Cards can display content and actions on a single topic

Cards can serve as entry points into deeper levels of detail or navigation, such as a music album or details on an upcoming vacation.

![Example world tour card.](../../_assets/lwujz8zw-3-efd10c4e18ea4ef4d442.png)

Card text and image show a clear hierarchy

![Card displaying connected details about a world tour.](../../_assets/lwujzmmd-4-598c5b2d2dadccacbbc6.png)

Use cards to display related information on a single subject

Cards can be displayed together in a grid, vertical list, or carousel Carousels show a collection of items that can be scrolled on and off the screen. [More on carousels](/m3/pages/carousel/overview) .

![4 cards together in a grid layout.](../../_assets/lwuk08jk-5-e2ae0426840490dcbd1e.png)

check Do

Cards can be shown together

![5 albums in a vertical list of cards.  ](../../_assets/lwuk0pob-6-cb57bd50c6f81a69c230.png)

close Don’t

Don't force content into cards when spacing, headlines, or dividers would create a simpler visual hierarchy

There are three card variants:

-   Elevated Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards

-   Filled Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards.

-   Outlined Outlined cards have a visual boundary around their container. This can provide greater emphasis than the other types.

Each provides the same legibility and functionality, so the variant you use depends on style alone.

![3 variants of cards.](../../_assets/lwuk16p3-7-e8ec5457ea13446f68f1.png)

1.  Elevated card
2.  Filled card 
3.  Outlined card

![Example elevated card.](../../_assets/lwuk25nc-8-5be0d05044dc32318a6d.png)

Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards

![Example filled card.](../../_assets/lwuk2m44-9-05f591c0ff7e863db74e.png)

Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards.

![Example outlined card.](../../_assets/lwuk337j-10-f9df2b933c4421a1c7e1.png)

Outlined cards have a visual boundary around the container. This can provide greater emphasis than the other variants.

## Anatomy

The card container is the only required element in a card. Card layouts can vary to support the kinds of content they contain. Below is a common configuration of elements.

![Diagram labeling the 6 parts of card anatomy.](../../_assets/eiTnWJl-s5HUIjPs1tfHU9HJp4izquC1-CiHPmdGA3Eq1YAw82dWNDHWYoQN1aUiXKSQm1jkq8uHW8i2-816a25258c918246c8f9.png)

1.  Container

2.  Image

3.  Button

4.  Supporting text

5.  Subhead

6.  Headline

### Container

Card containers hold all card elements. Their size is determined by the space those elements occupy. Card elevation is expressed by the container.

The card container is the only required element of a card. All other elements are optional.

![3 card containers with various elements: 1 with all elements except a button. 1 with a container, headline, supporting text, button. 1 with a container, headline, supporting text, 2 buttons.](../../_assets/lwuk4ddn-12-df7293f66bd2f1c7299f.png)

Card size is determined by the elements it contains

### Content blocks

Card contents are grouped into blocks. Content can have different levels of visual emphasis depending on importance.

Card layouts vary to support the kinds of content they contain.

![Diagram of card content blocks.](../../_assets/lwuk4w24-13-631e8d2e93fbbbf5eb33.png)

Cards can contain a headline, subhead, supporting text, media, and actions

### Dividers

[Dividers](/m3/pages/divider/specs) can separate regions in cards or indicate areas of a card that can expand.

![A divider running the entire width of the card.](../../_assets/lwuk5dl8-14-23ff56c2925c099f6d37.png)

1\. Use full-width dividers for content that can be expanded

![An inset divider indented from the edge of card.](../../_assets/lwuk5r9g-15-389cbbbde2fa3ea751cc.png)

1\. Use inset dividers, which don’t run the full width of a card, to separate related content

### Media

**Thumbnail**
Cards can include thumbnails for an avatar or logo.

**Image**
Cards can include photos, illustrations, and other graphics, such as weather icons.

**Video**
Cards can include video.

![A mobile chat app with: 5 cards with images, 1 card with a thumbnail avatar, and 1 card with a video. ](../../_assets/lwuk7ixf-16-0c987d03e4d572732d85.png)

Cards can contain thumbnails, images, and video

### Text

**Headline**
Headline text often communicates the subject of the card, such as the name of a photo album or article.

**Subhead**
Subheads are smaller text elements, such as an article byline or a tagged location.

**Supporting text**
Supporting text includes body content, such as an article summary or a restaurant description.

![card container with several elementsA tablet email app with an email summary card with multiple text elements.](../../_assets/lwukrum6-17-1f68b74e951928cac050.png)

Headline, subhead, and supporting text in a card

#### Layering text, icons, and images

It isn’t recommended to place text or icons on images. If it’s necessary, ensure the background image provides sufficient contrast for the text to meet accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/cards/accessibility) standards.

Add a translucent scrim or bounding shape beneath the text or icon to help ensure proper contrast.

![Layered text contrasts with the background image.](../../_assets/lwuke2rr-18-54c4645192a4ae298765.png)

exclamation Caution

Ensure that text on images meets accessible contrast standards

![Icon within a bounding shape, placed on an image.](../../_assets/lwukejwa-19-0845b76bb37c6067a57f.png)

exclamation Caution

When placing text or icons on images, consider using a bounding shape to ensure proper contrast

### Actions

#### **Primary action area**

Cards can be one large touch target triggering an expanded detail screen.

![The action area of a card contains rich media and supporting text.](../../_assets/lwukf67i-20-0938baf2a8c0b3a86db8.png)

Cards can include a primary action area that expands into a full-screen view

**Buttons**
Cards can include buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) for actions such as **Learn more** or **Add to cart**.

**Icon buttons**
Cards can include icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) for actions such as **Save**, **Heart**, or **Leave a 4-star review**.

**Selection controls**
Cards can also include chips Chips help people enter information, make selections, filter content, or trigger actions. [More on chips](/m3/pages/chips/overview) , sliders Sliders let users make selections from a range of values. [More on sliders](/m3/pages/sliders/overview) , checkboxes Checkboxes let users select one or more items from a list, or turn an item on or off. [More on checkboxes](/m3/pages/checkbox/overview) , and other selection controls.

**Linked text**
There can be a link in the supporting text on a card.

![Supplemental text and actions at the top and bottom of the card.](../../_assets/lwukfjtw-21-43c06f8f4d6341454e96.png)

Cards can include multiple action areas containing buttons, links, and other controls

![Album card with an option to give a star rating.](../../_assets/lwukg62l-22-356f9aeccc7417430318.png)

Cards can contain icon buttons like stars to rate content

![Card to purchase tickets with choice chips for 3 event times.](../../_assets/lwukgix5-23-64381e5d4d0ce62f201d.png)

Cards can contain choice chips in the action area

![Card with slider to control a song’s volume.](../../_assets/lwukgu3i-24-3625af9d15d17293f655.png)

Cards can contain a slider control in the action area

**Overflow menu**
Overflow menus contain related actions. They are typically placed in the upper-right or lower-right corner of a card.

![2 cards: 1 with an overflow menu in the upper-right corner, the other with it in the lower right.](../../_assets/lwukh83p-25-477b906dc5929e11db23.png)

Overflow menus are usually located in the upper-right or lower-right corner of a card

## Cards in a collection

Multiple cards can be grouped together into collections displayed in a grid, list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) , or carousel Carousels show a collection of items that can be scrolled on and off the screen. [More on carousels](/m3/pages/carousel/overview) . 

By default, cards in a collection are coplanar. They share the same resting elevation unless they're picked up or dragged A dragged state communicates when a user presses and moves an element. [More on dragged state](/m3/pages/interaction-states/applying-states#198c29c7-771e-4264-91e9-70c32b8902ec) .

![9 cards in a grid layout.](../../_assets/lwukhv18-26-5df40b5a78dca49cf470.png)

Multiple cards can be grouped into collections with a shared resting elevation

#### Filtering and sorting

Card collections can be filtered in a variety of ways, including by date or alphabetical order. If a collection can be filtered, the filter must apply to each card in the collection. 

Filter or sorting options should be placed outside of the card collection.

![A sort-by-date option placed above a card collection.](../../_assets/lwukig38-27-a444b09a31ea07f02424.png)

Card collections can be filtered in a variety of ways, including by date:
1\. A sort-by-date option is placed outside of the card collection 

Organize card collections so that they'e easy to use. Their layout Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/understanding-layout/overview) affects how they are perceived.

![A template for an 8-card collection layout.](../../_assets/lwukiwuu-28-4e01d27a691b62b34e7d.png)

Place cards in a collection in a straightforward, easy-to-use manner

### Grid

Cards can be displayed together in a grid.

Cards displayed in a grid

The default grid can be customized in code to show cards in staggered or mosaic grids.

![5 menu item cards in a mosaic grid.](../../_assets/lwukjfiq-30-80351a0b585084dfeb23.png)

Custom mosaic grid

![4 menu item cards in a staggered grid.](../../_assets/lwukk75c-31-348f1c467b730abf7e03.png)

Custom staggered grid

### Vertical list

Cards can be displayed together in a vertical list.

Cards can be shown in a vertical list

### Carousel

Cards can be displayed together in a horizontal row or carousel Carousels show a collection of items that can be scrolled on and off the screen. [More on carousels](/m3/pages/carousel/overview) .

Cards displayed together in a horizontal row or carousel

## Adaptive design

As cards scale to adapt to different [breakpoints](/m3/pages/breakpoints), their position and alignment can also change.

Cards and their elements can align left, right, or center as the layout scales.

![2 cards on a mobile screen row expand to 4 cards on a tablet screen row. ](../../_assets/lwukkvy8-34-9082b4ae486477ef1ea3.png)

Card position and alignment changes as the screen size changes

### Ergonomics

Adjust the layout Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/understanding-layout/overview) of cards to meet the ergonomic needs of large screens. 

For example, a horizontally-oriented card in a compact breakpoint Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) may become a larger, vertically-oriented card in an expanded breakpoint Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , with more space for images and text on the larger screen.

![Card sizes change from mobile to tablet, with larger images in the tablet layout.](../../_assets/lwuklb57-35-8272774b3b004647b8a9.png)

Adjust the card layout so content remains the main focus on large screens

### Visual presentation

To adjust the presentation of content-focused components, begin with spacing. 

Allow components like lists Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) , cards, and images to optimize space while filling the region of a screen that suits a device breakpoint’s ergonomic needs.

![2 cards with optimized space: 1 narrow rectangle, 1 wide square.](../../_assets/lwukluzj-36-2f8fc357c782adf61731.png)

Spacing adjusts for components such as cards, lists, and images

![2 examples of the same card: 1 vertical with an image at the top, 1 horizontal with an image on the left.](../../_assets/lwukmfqz-37-409fd772bb9d94d4add6.png)

Example of the same card with two different orientations and element positioning

### Column-based layouts

In mobile layouts, components such as lists Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) or cards are stretched to fit the full width of the screen without compromising visual quality or user experience. When designing for large screens with an expanded breakpoint Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded breakpoints](/m3/pages/breakpoints/expanded) , use multiple columns to display content.

Avoid extending UI elements across the screen when possible. On larger screens, rearrange groups of related cards into horizontal rows or carousels Carousels show a collection of items that can be scrolled on and off the screen. [More on carousels](/m3/pages/carousel/overview) , to allow for better content organization.

![3 related cards in a carousel.](../../_assets/lwukn6ma-38-ff0c4a298270b0dcca97.png)

When designing for large screens, use multiple columns to display content

### Small screens

On smaller screens with the compact breakpoint Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact breakpoints](/m3/pages/breakpoints/compact) , consider swapping cards for lists Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) , which can display images and text in a more compact form. 

Make sure that controls, actions, and other component-specific elements are maintained.

Certain devices or user contexts require different components to meet platform expectations

## Behavior

### Expanding

Cards can use a [container transform](/m3/pages/motion-transitions/transition-patterns#b67cba74-6240-4663-a423-d537b6d21187) transition pattern to reveal additional content. Reserve this pattern for hero moments that are meant to be expressive.

A card expands to fill the full screen using a parent-child transition

check Do

Expand a card to reveal information

close Don’t

Don’t scroll within a card to reveal information

### Navigation

Cards can use a [forward and backward](/m3/pages/motion-transitions/transition-patterns#df9c7d76-1454-47f3-ad1c-268a31f58bad) transition pattern to navigate between screens at consecutive levels of hierarchy. This pattern has a simpler motion style compared to container transform, which makes it suitable for common navigation transitions.

Cards can use a forward and backward transition pattern to navigate between screens

### Gestures

#### Swipe

A swipe gesture Gestures are all the ways people interact with UI elements using touch. [More on gestures](/m3/pages/gestures) can be performed on a single card at a time, anywhere on that card.

It can be used to:

-   Dismiss a card
-   Change the state States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) of a card, such as flagging or archiving it

check Do

A card should only have one swipe action assigned to it

close Don’t

Cards shouldn’t contain content that can be swiped, such as an image carousel or pagination. Also, swipe gestures shouldn’t cause portions of cards to detach upon swiping.

#### Pick up & move

The pick-up-and-move gesture Gestures are all the ways people interact with UI elements using touch. [More on gestures](/m3/pages/gestures) allows users to move and reorder cards in a collection.

check Do

When moving a card, increase its elevation

close Don’t

Don’t let cards bump other elements out of the way. When a card is picked up, it appears in front of all elements, except app bars and navigation.

#### Scrolling

Card content that’s taller than the maximum card height is truncated and doesn’t scroll, but can be displayed by expanding the height of a card.  

A card can expand beyond the maximum height of the screen, in which case the card scrolls within the screen.

check Do On a mobile device, cards can expand to reveal more content, scrolling within the screen. Content within cards doesn’t scroll.

close Don’t

On a mobile device, cards can't internally scroll, as it could cause two scroll bars to be displayed

#### Scrolling on desktop

On a desktop device, card content can expand and scroll within a card.

On a desktop, content can expand and scroll within a card
