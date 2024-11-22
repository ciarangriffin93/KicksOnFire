This is the TESTING file 

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Note |
| --- | --- | --- | --- |
| home | index.html | ![screenshot](/docs/testing_images/home-html-ws3.png) | pass |
| products | products.html | ![screenshot](/docs/testing_images/products-html-ws3.png) | pass |
| checkout | checkout.html | ![screenshot](/docs/testing_images/checkout-html-ws3.png) | pass |
| checkout success | checkout_success.html | ![screenshot](/docs/testing_images/checkout_success-html-ws3.png) | pass |
| about | about.html | ![screenshot](/docs/testing_images/about-html-ws3.png) | pass |
| news | news.html | ![screenshot](/docs/testing_images/blog-html-ws3.png) | pass |
| add a product | add_product.html | ![screenshot](/docs/testing_images/products_add-html-ws3.png) | pass |
| edit a product | edit_product.html | ![screenshot](/docs/testing_images/products_edit-html-ws3.png) | pass |
| order_history | profile.html | ![screenshot](/docs/testing_images/order_history-html-ws3.png) | pass |
| bag | bag.html | ![screenshot](/docs/testing_images/bag-html-ws3.png) | pass |

## CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files.

The CSS validations, as they are all the same.

![css validation](/docs/testing_images/css-validator.png)

| CSS File | Errors | Warnings |
| ---- | ------ | -------- |
| Base CSS | 0 | 0 |
| Profile CSS | 0 | 0 |

## Python

[PEP8 CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python files that were created.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bag | app.py | ![screenshot](/docs/testing_images/bag-apps.png) | all clear, no errors found |
| bag | context.py | ![screenshot](/docs/testing_images/bag-contexts.png) | all clear, no errors found |
| bag | views.py | ![screenshot](/docs/testing_images/bag-views.png) | all clear, no errors found |
| blog | admin.py | ![screenshot](/docs/testing_images/blog-admin.png) | all clear, no errors found |
| blog | models.py | ![screenshot](/docs/testing_images/blog-models.png) | all clear, no errors found |
| blog | views.py | ![screenshot](/docs/testing_images/blog-views.png) | all clear, no errors found |
| Checkout | admin.py | ![screenshot](/docs/testing_images/checkout-admin.png) | all clear, no errors found |
| checkout | forms.py | ![screenshot](/docs/testing_images/checkout-forms.png) | all clear, no errors found |
| checkout | models.py | ![screenshot](/docs/testing_images/checkout-models.png) | all clear, no errors found |
| checkout | urls.py | ![screenshot](/docs/testing_images/checkout-urls.png) | all clear, no errors found |
| checkout | views.py | ![screenshot](/docs/testing_images/checkout-views.png) | all clear, no errors found |
| checkout | webhook_headler | ![screenshot](/docs/testing_images/checkout-webhook_handler.png) | At two spaces before inline comment and i use to put # noqa |
| checkout | signals.py | ![screenshot](/docs/testing_images/checkout-signals.png) | all clear, no errors found |
| contact | admin.py | ![screenshot](/docs/testing_images/contact-admin.png) | all clear, no errors found |
| contact | models.py | ![screenshot](/docs/testing_images/contact-models.png) | all clear, no errors found |
| contact | views.py | ![screenshot](/docs/testing_images/contact-views.png) | at two spaces before inline comment and i use to put # noqa |
| products | admin.py | ![screenshot](/docs/testing_images/products-admin.png) | all clear, no errors found |
| products | forms.py | ![screenshot](/docs/testing_images/products-forms.png) | at two spaces before inline comment and i use to put # noqa|
| products | models.py | ![screenshot](/docs/testing_images/products-models.png) | all clear, no errors found |
| products | views.py | ![screenshot](/docs/testing_images/products-views.png) | at two spaces before inline comment and i use to put # noqa |
| profile | forms.py | ![screenshot](/docs/testing_images/profile-forms.png) | all clear, no errors found |
| profile | models.py | ![screenshot](/docs/testing_images/profile-models.png) | all clear, no errors found |
| wishlist | models.py | ![screenshot](/docs/testing_images/wishlist-models.png) | all clear, no errors found |
| wishlist | views.py | ![screenshot](/docs/testing_images/wishlist-views.png) | at two spaces before inline comment and i i use to put # noqa |

## Lighthouse 

All of the pages for this project were tested using [pagespeed](https://pagespeed.web.dev/) the website operates efficiently on both mobile and desktop devices.

| Page | Lighthouse Scores - Desktop | Note |
| ---- | ----------------- | ---- |
| Home |   ![home](/docs/testing_images/home-desktop-pagespeed.png) | Minor warnings |
| Products |   ![products](/docs/testing_images/product-desktop-pagespeed.png) | Minor warnings |
| Blog |   ![blog](/docs/testing_images/blog-desktop-pagespeed.png) | Minor warnings |
| Wishist |   ![wishlist](/docs/testing_images/wishlist-desktop-pagespeed.png) | Minor warnings |

| Page | Lighthouse Scores - Molilbe | Note |
| ---- | ----------------- | ---- |
| Home |   ![home](/docs/testing_images/home-mobile-pagespeed.png) | Minor warnings |
| Products |   ![products](/docs/testing_images/products-mobile-pagespeed.png) | Minor warnings |
| Blog |   ![blog](/docs/testing_images/blog-mobile-pagespeed.png) | Minor warnings |
| Wishist |   ![wishlist](/docs/testing_images/wishlist-mobile-pagespeed.png) |

## Manual Testing

Testing was conducted on a desktop using the Chrome browser.

| TEST | ACTION | EXPECTATION | RESULT | PASS/FAIL
| -------- | ---------- | --------------- | -----------|--------|
| Shop now | click on button | User should be forwarded to all products page | Worked as expected | Pass |
| Products  | click on button | User should be forwarded to products detail page | Worked as expected | Pass |
| Keep shopping | click on button | User should be able to go back to products page | Worked as expected | Pass |
| Keep shopping | click on button | User should be able to go back to products form products detail page | Worked as expected | Pass |
| Add to shopping cart | click on button | User should be able to add an item to the shopping car | Worked as expected | Pass |
| Shopping cart | click on button | User should be able to view the shopping cart | Worked as expected | Pass |
| Udpate item | click on button | User should be able to update quantity in shopping cart | Worked as expected | Pass |
| Remove item | click on button | User should be able to remove an item from the shopping cart | Worked as expected | Pass |
| wishlist | click on button | User should be able to save products to the wishlist | Worked as expected | Pass |
| wishlist Remove | click on button | User should be able to remove an item from the wishlist | Worked as expected | Pass |
| Secure checkout | click on button | User should be able to make a secure checkout from shopping cart | Worked as expected | Pass |
| Keep shopping | click on button | User should be able to go back to products form the shopping cart | Worked as expected | Pass |
| History order | click on button | User should be able to view details of old orders in their profile | Worked as expected | Pass |
| Newsletter subscription | click on button | User should be able to subscribe | Worked as expected | Pass |
| Social media | click on button | User should be forwarded to facebook, GitHub and linkedin | Worked as expected | Pass |
| Register | click on button | User should be forwarded to the signup form | Worked as expected | Pass |
| Signup | click on button | User should be forwarded to the homepage as logged-in user | Worked as expected | Pass |

## Responsiveness

The website is fully responsive and adjusts perfectly to various screen sizes.

| Device | Home | About | Blog | Blog Detail | Product | Product Detail | Contact | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Desktop | ![screenshot](/docs/testing_images/desktop-home-resp.png) | ![screenshot](/docs/testing_images/desktop-about-resp.png) | ![screenshot](/docs/testing_images/desktop-blog-resp.png) | ![screenshot](/docs/testing_images/desktop-blog-detail-resp.png) | ![screenshot](/docs/testing_images/desktop-products-resp.png) | ![screenshot](/docs/testing_images/desktop-products-detail-resp.png) | ![screenshot](/docs/testing_images/desktop-contact-resp.png) | The performance meets the expected standard. |
| Mobile | ![screenshot](/docs/testing_images/mobile-home-resp.png) | ![screenshot](/docs/testing_images/mobile-about-resp.png) | ![screenshot](/docs/testing_images/mobile-blog-resp.png) | ![screenshot](/docs/testing_images/mobile-blog-detail-resp.png) | ![screenshot](/docs/testing_images/mobile-products-resp.png) | ![screenshot](/docs/testing_images/mobile-product-detail-resp.png) | ![screenshot](/docs/testing_images/mobile-contact-resp.png) | The performance meets the expected standard. |
| Tablet | ![screenshot](/docs/testing_images/tablet-home-resp.png) | ![screenshot](/docs/testing_images/tablet-about-resp.png) | ![screenshot](/docs/testing_images/tablet-blog-resp.png) | ![screenshot](/docs/testing_images/tablet-blog-detail-resp.png) | ![screenshot](/docs/testing_images/tablet-products-resp.png) | ![screenshot](/docs/testing_images/mobile-product-detail-resp.png) | ![screenshot](/docs/testing_images/tablet-contact-resp.png) | The performance meets the expected standard. |


### Browser Compatibility

I tested on various browsers; purchases were made, articles and products were added, edited, or deleted, and all features were functioning properly.

- Chrome 
- Firefox

| Browser | Issue | Functionality |
|---------|-------|---------------|
| Chrome  | None | All Intact |
| Firefox | None  | All Intact    |

### Dev Tools/Real World Device Testing

To ensure the Kicksonfire  e-commerce platform was fully responsive, comprehensive testing was carried out across a variety of devices using Google Dev Tools. All features of the platform were tested on these devices to verify the responsiveness and functionality. Below is a summary of the testing results and any issues that were identified, along with the fixes implemented.

**Dev Tools Device Testing - all features tested, issues noted below**
| Device  | Feature    | Issue  | Fix  |
| ------- | ---------- | ------ |------|
| iPhone 12 Pro | All features | None | No issues detected.  |
| Samsung Galaxy s20 | All features | None | No issues detected. |
| iPad Pro | All features | None | No issues detected. |

### BUG

* PostgreSQL Database Issue: Initially, there were problems with the PostgreSQL database, so I made the decision to switch to a new PostgreSQL server. Since then, everything has been running smoothly.

* Broken +/- Buttons on Bag/Cart Page: The +/- buttons on the bag/cart page were malfunctioning, so I resolved the issue by updating the quantity_input.js file. The fix was successful, and now customers can adjust quantities without any problems.

No Known Unresolved Bugs: The system is currently stable with no outstanding issues.


