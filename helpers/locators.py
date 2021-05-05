# Common constants
WARNING_ALERT_CSS = "div.pf-c-alert.pf-m-warning h4.pf-c-alert__title"
WARNING_ALERT_DESCRIPTION_CSS = "div.pf-c-alert.pf-m-warning div.pf-c-alert__description"
CLOSE_WARNING_ALERT_CSS = "div.pf-c-alert__action button"

# Login page
LOGIN_LINK_TEXT = "Log In"
USER_NAME_ID = "username"
LOGGED_IN_USERNAME = "a.p2-header__login"
PASSWORD_ID = "password"
LOGIN_NEXT_BUTTON_ID = "login-show-step2"
LOGIN_BUTTON_ID = "kc-login"
LOGGED_IN_USER_PARTIAL_TEXT = "Log Out"

# Display module page
MODULE_DISPLAY_TITLE_CSS = "div.pf-l-level h1"
MODULE_DISPLAY_PUBLISH_BUTTON_ID = "publishButton"
    # "button.pf-c-button.pf-m-primary"
MODULE_DISPLAY_UNPUBLISH_BUTTON_ID = "unpublishButton"
    # "button.pf-c-button.pf-m-primary"
MODULE_DISPLAY_PREVIEW_BUTTON_CSS = "div.pf-c-card__header div:nth-child(4) button"
MODULE_DISPLAY_PUBLISH_STATUS_CSS = "div.pf-l-level:nth-child(6) div:nth-child(5) div.pf-c-content p span"
MODULE_METADATA_WARNING_CSS = "div.pf-c-alert__description"
ADD_METADATA_BUTTON_XPATH = "//button[contains(text(),'Add metadata')]"
EDIT_METADATA_MODAL_TITLE_CSS = "h1.pf-c-title.pf-m-2xl"
PRODUCT_NAME_DROPDOWN_CSS = "select[aria-label='FormSelect Product'].pf-c-form-control"
PRODUCT_VERSION_DROPDOWN_CSS = "select#productVersion"
PRODUCT_USECASE_DROPDOWN_CSS = "select[aria-label='FormSelect Usecase'].pf-c-form-control"
PRODUCT_URLFRAGMENT_CSS = "input#url-fragment"
EDIT_METADATA_SAVE_CSS = "footer.pf-c-modal-box__footer button.pf-c-button.pf-m-primary"
EDIT_METADATA_CANCEL_CSS = "footer.pf-c-modal-box__footer button.pf-c-button.pf-m-secondary"
EDIT_METADATA_WARNING_CSS = "span.pf-u-screen-reader"
UPDATE_SUCCESS_MESSAGE_CSS = "div.pf-c-alert.pf-m-success div.pf-c-alert__description"
PRODUCT_INFO_CSS = "section.pf-c-page__main-section.pf-m-light div.pf-l-level:nth-child(6)>div:nth-child(1)"
COPY_URL_LINK_CSS = "a#permanentURL"
VIEW_ON_PORTAL_LINK_CSS = "section.pf-c-page__main-section.pf-m-light div:nth-child(3) span:nth-child(1) a"
VIEW_MODULE_TYPE_CSS = "div.pf-l-level:nth-child(6) div:nth-child(3) > div.pf-c-content"
UPLOADED_DATE_MODULE_PAGE_CSS = "section.pf-c-page__main-section.pf-m-light div:nth-child(6) div:nth-child(4) span"
PUBLISHED_DATE_MODULE_PAGE_CSS = "section.pf-c-page__main-section.pf-m-light div:nth-child(6) div:nth-child(5) span"
MODULES_INCLUDED_LIST_CSS = "div.pf-c-content ul li a"
DRAFT_CARD = "article.pf-c-card-draft"
PUBLISHED_CARD = "article.pf-c-card.pf-m-selected"
UPLOAD_TIME_ON_DRAFT_CARD = "article.pf-c-card-draft div.pf-c-card__body div.pf-c-content:nth-child(1) p:nth-child(2)"
UPLOAD_TIME_ON_PUBLISHED_CARD = "article.pf-m-selected div.pf-c-card__body div.pf-c-content:nth-child(1) p:nth-child(2)"
DRAFT_CARD_TITLE = "article.pf-c-card-draft div.pf-c-card__header div strong"
PUBLISHED_CARD_TITLE = "article.pf-m-selected div.pf-c-card__header div strong span"
ATTRIBUTE_FILE_CSS = "div.pf-c-card__body div.pf-c-content:nth-child(3) p:nth-child(2)"
CARDS_ON_DETAILS_PAGE_CSS = "article.pf-c-card div div article.pf-c-card"

# Customer portal
MODULE_TITLE_ON_PORTAL_ID= "rhdocs-header"
PRODUCT_NAME_ON_PREVIEW_CSS = "span.rhdocs-product-name"
PRODUCT_VERSION_ON_PREVIEW_CSS = "span.rhdocs-product-version"
UPDATED_DATE_ON_PORTAL_CSS = "li.rh-docs-details-item.rhdocs-updated-date"
UPDATED_DATE_ON_PREVIEW_CSS = "li.rh-docs-details-item.rhdocs-updated-date"
PUBLISHED_DATE_ON_PORTAL_CSS = "li.rh-docs-details-item.rhdocs-published-date"
PUBLISHED_DATE_ON_PREVIEW_CSS = "li.rh-docs-details-item.rhdocs-published-date"
MODULE_NOT_FOUND_CLASS_NAME = "fcc_module_body"
MODULE_FOUND_ID = "rhdocs"
SEARCH_BODY_ON_PREVIEW_CSS = "section.sectionbody p:nth-child(2)"
MODULE_BODY_CSS = "cp-documentation.PFElement"
MODULE_BODY_ON_PORTAL_CSS = "cp-documentation#rhdocs"
MODULE_BODY_CONTENT_CSS = "cp-documentation#doc-content"
MODULE_TITLE_ON_PORTAL_CSS = "header#rhdocs-header div h1"
CP_PRODUCT_NAME_CSS = "header#rhdocs-header div.rhdocs-products span.rhdocs-product-name"
CP_PRODUCT_VERSION_CSS = "header#rhdocs-header div.rhdocs-products span.rhdocs-product-version"
LEGAL_NOTICE_ON_PREVIEW_CSS = "a.rh-docs-legal-notice__link"
LEGAL_NOTICE_ON_PORTAL_CSS = "article#rhdocs-content div.rh-docs-legal-notice a.rh-docs-legal-notice__link"
CONTENT_RELATED_GUIDES_RESOURCES = "details.related-topic-content__wrapper--for-guide aside div.sectionbody"
CONTENT_RELATED_TO_GUIDES = "details.related-topic-content__wrapper--for-guide"

# Menu
MENU_GIT_IMPORT_LINK_TEXT = "Git Import"
# MENU_PRODUCTS_LINK_TEXT = "Products"
MENU_PRODUCTS_LINK_XPATH = "//button[contains(text(),'Products')]"
MENU_NEW_PRODUCT_LINK_TEXT = "New Product"
MENU_PRODUCT_LISTING_LINK_TEXT = "Product Listing"
MENU_SEARCH_PAGE_LINK_TEXT = "Search"

# Git import page
GIT_REPO_URL_TEXTBOX_CSS = "input#repository-url"
GIT_REPO_BRANCH_TEXTBOX_CSS = "input#branch-name"
GIT_REPO_SUBMIT_BUTTON_CSS = "button.pf-c-button.pf-m-primary"
GIT_IMPORT_REQUEST_SUBMITTED_TITLE = "//header[@class='pf-c-modal-box__header']/h1"
GIT_IMPORT_REQUEST_SUBMITTED_YES = "footer.pf-c-modal-box__footer button.pf-m-primary"
REPO_URL_INVALID_ERROR_CSS = "div.pf-c-alert.pf-m-danger h4.pf-c-alert__title"

# Search page
FIRST_MODULE_CHECKBOX_XPATH = "//div[@id='data-rows'][2]/div[@class='pf-c-check checkbox']"
DELETE_BUTTON_TOP_XPATH = "//div[@id='data-rows'][1]/button"
DELETE_CONFIRMATION_TITLE_CSS = "div.pf-c-modal-box.pf-m-sm h1"
DELETE_CONFIRMATION_YES_CSS = "div.pf-c-modal-box__footer button.pf-c-button.pf-m-primary"
DELETE_SUCCESS_MODAL_TITLE_XPATH = "//h1[text()='Success']"
DELETE_SUCCESS_MODAL_OK_XPATH = "//button[contains(text(),'OK')]"
MODULE_LIST = "div#data-rows"
CHECKBOX_BY_TITLE = "//a[contains(text(), 'module_title_placeholder')]/../..//preceding-sibling::div[@class='pf-c-check checkbox']"
MODULES_WITH_SOURCE_NAME = "//span[contains(text(),'{}')]"
MODULES_WITH_CURRENT_DATE = "//span[contains(text(),'{}')]"
SEARCH_BOX_ID = "searchFilterInput"
SEARCH_BUTTON_CSS = "input#searchFilterInput+button.pf-c-button.pf-m-control"
SORT_BY_DROPDOWN_CSS = "select#sortForm"
SORT_ORDER_BUTTON_CSS = "select#sortForm+button.pf-c-button.pf-m-control"
MODULE_TITLE_CSS = "div.pf-c-data-list__cell.pf-m-flex-2 a"
MODULE_TYPE_DROPDOWN_CSS = "div.filters-bar__dropdown-filter--content-type"
CONCEPT_CHECKBOX_ID = "pf-random-id-3-CONCEPT"
PROCEDURE_CHECKBOX_ID = "pf-random-id-3-PROCEDURE"
REFERENCE_CHECKBOX_ID = "pf-random-id-3-REFERENCE"
# FIRST_MODULE_LISTED_CSS = "div#data-rows:nth-child(3) div div.pf-c-data-list__cell a"
MODULE_TYPE_LIST_CSS = "div#data-rows div.pf-c-data-list__item-content div.pf-c-data-list__cell:nth-child(4) span"
SEARCH_MODULE_XPATH = "//div[@class='pf-c-data-list__cell pf-m-flex-2']/a"
NO_MODULE_FOUND_CSS = "h4.pf-c-alert__title"
CANCEL_BUTTON_XPATH = "//div[@class='pf-c-alert__action']/button"
SELECT_PRODUCT_NAME_CSS = "select#productForm"
SELECT_PRODUCT_VERSION_CSS = "select#productVersionForm"
PRODUCT_FILTER_DISPLAY_XPATH = "//div[@class='pf-c-chip-group pf-m-category']"
PRODUCT_VERSION_DISPLAY_PAGE_XPATH = "//div[@class='pf-l-level'][5]//div[1]/div/p/span"
SEARCH_RESULTS = "ul.pf-c-data-list"

#help_documentation_page
HELP_ICON_CLASS_NAME = "button.pf-c-dropdown__toggle.pf-m-plain"
USER_GUIDE_LINK_TEXT = "User Guide"
TITLE_OF_USER_GUIDE_CSS = "div.rhdocs__header__primary-wrapper h1"
USER_GUIDE_PARENT_CSS = "cp-documentation#doc-content"

# New Product page
PRODUCT_NAME_TEXTBOX_ID = "product_name_text"
PRODUCT_DESCRIPTION_TEXTBOX_ID = "product_description_text"
SAVE_PRODUCT_BUTTON_CSS = "button.pf-c-button.pf-m-primary"
PRODUCT_URL_FRAGMENT_TEXTBOX_ID = "product_url_fragment_text"
NEW_PRODUCT_VERSION_TEXTBOX_ID = "new_version_name_text"
PRODUCT_VERSION_URL_FRAGMENT_ID = "new_version_url_fragment"

# Product Listing page
PRODUCT_LIST_UL_CLASS_NAME = "pf-c-data-list"
PRODUCT_NAMES_LI_ID = "{data.name}"
PRODUCT_NAME_LIST_CSS = "div.pf-c-data-list__cell > span"
PRODUCT_NAMES_LIST_CLASS_NAME = "pf-c-data-list__item"
PRODUCT_NAME_LI_DROPDOWN_CLASS_NAME = "pf-c-options-menu__toggle pf-m-plain"
PRODUCT_DETAILS_BUTTON_CLASS_NAME = "pf-c-options-menu__menu-item"
PRODUCT_VERSIONS_UL_CLASS_NAME = "pf-c-list"
PRODUCT_VERSIONS_LI_TAG_NAME = "li"
VERSION_URL_FRAGMENT_ID = "url_fragment_text"
PRODUCT_VERSION_SAVE_BUTTON_CSS = "button.pf-c-button.pf-m-primary"

#PReview
DOCUMENT_TITLE = "header#rhdocs-header h1"
DOCUMENT_TITLE_CP = "header#rhdocs-header-external"
IMAGE_CSS = "span.image img"
ASSEMBLY_BODY_CSS = "div.rhdocs"
ASSEMBLY_BODY_PREVIEW_CSS = "body cp-documentation"
ATTRIBUTE_ON_PREVIEW_CSS = "section > p:nth-child(1)"

#search beta
NO_MODULE_RESULTS_FOUND_CSS = "div.search-results__section--module div.pf-c-empty-state__body"
NO_ASSEMBLY_RESULTS_FOUND_CSS = "div.search-results__section--assembly div.pf-c-empty-state__body"
FILTER_BY_REPO_SEARCH_BAR_XPATH= "//input[@placeholder='Filter']"
FILTER_BY_REPO_SECTION_CLASS_NAME = "filters-drawer--by-repo"
SELECT_REPO_CHECKBOX_CLASS_NAME = "pf-c-check__label"
SEARCH_REPO_XPATH = "//li//label[contains(text(),'uploader-sample-repo-pantheon2')]"
TOGGLE_ID = "filters-bar__toolbar-toggle"
CONTENT_TYPE_CLASS_NAME = "filters-bar__dropdown-filter--content-type"
CANCEL_BUTTON_ON_REPO_SEARCH_BAR_CLASS_NAME = "pf-c-search-input__clear"
REPOSITORY_NAME_XPATH = "//td[@data-label='Repository']"
FILTER_BY_REPO_TOGGLE_XPATH = "//span[contains(text(), 'By repository')]"
REPO_LIST_XPATH = "//div[@aria-label='Repository List']"
MODULES_CSS = "div.search-results__section--module tbody"
ASSEMBLY_CSS = "div.search-results__section--assembly tbody"
MODULES_TOGGLE_BUTTON_XPATH = "//span[contains(text(),'Modules')]"
ASSEMBLY_TOGGLE_BUTTON_XPATH = "//span[contains(text(),'Assemblies')]"
MODULE_ASSEMBLY_TOGGLE_XPATH = "//button[@class='pf-c-expandable-section__toggle' and @aria-expanded='false']"
MODULE_TITLES_CSS = "div.search-results__section--module th:nth-child(2)"
ASSEMBLY_TITLES_CSS = "div.search-results__section--assembly th:nth-child(2)"
REPOSITORY_CHECKBOX_CSS = "label.pf-c-check__label"
# below locators added for future use
STATUS_FILTER_CLASS_NAME = "filters-bar__dropdown-filter--status"
DRAFT_STATUS_CLASS_NAME = "dropdown-filter__option--draft"
STATUS_TOOLBAR_CHIP_CLASS_NAME = "pf-m-chip-group"
SEARCH_TITLE_CSS = "#textInput span input"
TITLE_SEARCH_ICON_CSS = "button.pf-c-button.pf-m-control"
CONCEPT_CONTENT_TYPE_FILTER_CLASS_NAME = "dropdown-filter__option--concept"
FIRST_MODULE_LISTED_CSS = "div.search-results__section--module tbody tr:nth-child(1) th div a"
FIRST_LISTED_ASSEMBLY_CSS = "div.search-results__section--assembly tbody tr:nth-child(1) th div a"
FILTER_CHIP_LIST_CSS = "ul.pf-c-chip-group__list li div span"
ALL_MODULE_TITLES = "tbody tr th div a"