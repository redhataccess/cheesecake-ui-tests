# Common constants
WARNING_ALERT_CSS = "div.pf-c-alert.pf-m-warning h4.pf-c-alert__title"
WARNING_ALERT_DESCRIPTION_CSS = "div.pf-c-alert.pf-m-warning div.pf-c-alert__description"
CLOSE_WARNING_ALERT_CSS = "div.pf-c-alert__action button"

# Login page
LOGIN_TAB_XPATH = "//*[@href='#/login']"
USER_NAME_ID = "username"
PASSWORD_ID = "password"
LOGIN_BUTTON_CLASS_NAME = "pf-m-primary"
LOGGED_IN_USER_PARTIAL_TEXT = "Log Out"

# Display module page
MODULE_DISPLAY_TITLE_CSS = "div.pf-c-content h1"
MODULE_DISPLAY_PUBLISH_BUTTON_CSS = "div.pf-c-data-list__cell button.pf-c-button.pf-m-primary"
    # "button.pf-c-button.pf-m-primary"
MODULE_DISPLAY_UNPUBLISH_BUTTON_CSS = "div.pf-c-data-list__cell button.pf-c-button.pf-m-primary"
    # "button.pf-c-button.pf-m-primary"
MODULE_DISPLAY_PREVIEW_BUTTON_CSS = "button.pf-c-button.pf-m-secondary"
MODULE_DISPLAY_PUBLISH_STATUS_XPATH = "//div[contains(text(),'Not published')]"
MODULE_METADATA_WARNING_CSS = "div.pf-c-alert__description"
EDIT_METADATA_DROPDOWN_CSS = "div.pf-c-data-list__cell div.pf-c-dropdown button.pf-c-dropdown__toggle.pf-m-plain"
EDIT_METADATA_BUTTON_CSS = "button.pf-c-dropdown__menu-item"
EDIT_METADATA_MODAL_TITLE_CSS = "h1.pf-c-title.pf-m-2xl"
PRODUCT_NAME_DROPDOWN_CSS = "select[aria-label='FormSelect Product'].pf-c-form-control"
PRODUCT_VERSION_DROPDOWN_CSS = "select#productVersion"
PRODUCT_USECASE_DROPDOWN_CSS = "select[aria-label='FormSelect Usecase'].pf-c-form-control"
PRODUCT_URLFRAGMENT_CSS = "input#url-fragment"
EDIT_METADATA_SAVE_CSS = "div.pf-c-modal-box__footer button.pf-c-button.pf-m-primary"
EDIT_METADATA_CANCEL_CSS = "div.pf-c-modal-box__footer button.pf-c-button.pf-m-secondary"
EDIT_METADATA_WARNING_CSS = "span.pf-u-screen-reader"
UPDATE_SUCCESS_MESSAGE_CSS = "div.pf-c-alert.pf-m-success div.pf-c-alert__description"
PRODUCT_INFO_CSS = "div.pf-c-data-list__item-row:nth-child(2) div.pf-c-data-list__item-content div.pf-c-data-list__cell.pf-m-flex-2 span"
COPY_URL_LINK_CSS = "a#permanentURL"
VIEW_ON_PORTAL_LINK_CSS = "section.pf-c-page__main-section.pf-m-light div:nth-child(4) span:nth-child(1) a"
VIEW_MODULE_TYPE_CSS = "div.pf-c-data-list__item-row:nth-child(2) div div.pf-c-data-list__cell:nth-child(4) span"
UPLOADED_DATE_MODULE_PAGE_CSS = "div.pf-c-data-list__item-row:nth-child(2) div.pf-c-data-list__item-content div.pf-c-data-list__cell:nth-child(3)"
PUBLISHED_DATE_MODULE_PAGE_CSS = "div.pf-c-data-list__item-row:nth-child(2) div div.pf-c-data-list__cell:nth-child(2) span"

# Customer portal
MODULE_BODY_ON_PORTAL_CSS = "cp-documentation#rhdocs"
MODULE_TITLE_ON_PORTAL_CSS= "header#rhdocs-header"
PRODUCT_NAME_CSS = "span.rhdocs-product-name"
PRODUCT_VERSION_CSS = "span.rhdocs-product-version"
UPDATED_DATE_ON_PORTAL_CSS = "li.rh-docs-details-item.rhdocs-updated-date"
PUBLISHED_DATE_ON_PORTAL_CSS = "li.rh-docs-details-item.rhdocs-published-date"
MODULE_NOT_FOUND_CSS = "div.fcc_module_body"
MODULE_FOUND_ID = "rhdocs"

# Menu
MENU_GIT_IMPORT_LINK_TEXT = "Git Import"
MENU_PRODUCTS_LINK_TEXT = "Products"
MENU_NEW_PRODUCT_LINK_TEXT = "New Product"
MENU_PRODUCT_LISTING_LINK_TEXT = "Product Listing"
MENU_SEARCH_PAGE_LINK_TEXT = "Search"

# Git import page
GIT_REPO_URL_TEXTBOX_CSS = "input#repository-url"
GIT_REPO_BRANCH_TEXTBOX_CSS = "input#branch-name"
GIT_REPO_SUBMIT_BUTTON_CSS = "button.pf-c-button.pf-m-primary"
GIT_IMPORT_REQUEST_SUBMITTED_TITLE = "//div[@role='dialog']/h1"
GIT_IMPORT_REQUEST_SUBMITTED_YES = "div.pf-c-modal-box__footer button.pf-m-primary"
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
MODULE_TYPE_DROPDOWN_CSS = "#moduleTypeForm"
FIRST_MODULE_LISTED_CSS = "div#data-rows:nth-child(3) div div.pf-c-data-list__cell a"
MODULE_TYPE_LIST_CSS = "div#data-rows div.pf-c-data-list__item-content div.pf-c-data-list__cell:nth-child(4) span"

# New Product page
PRODUCT_NAME_TEXTBOX_ID = "product-name"
PRODUCT_DESCRIPTION_TEXTBOX_ID = "product-description"
SAVE_PRODUCT_BUTTON_CLASS_NAME = "pf-c-button.pf-m-primary"

# Product Listing page
PRODUCT_LIST_UL_CLASS_NAME = "pf-c-data-list"
PRODUCT_NAMES_LI_ID = "{data.name}"
PRODUCT_NAMES_LIST_CLASS_NAME = "pf-c-data-list__item"
PRODUCT_NAME_LI_DROPDOWN_CLASS_NAME = "pf-c-options-menu__toggle pf-m-plain"
PRODUCT_DETAILS_BUTTON_CLASS_NAME = "pf-c-options-menu__menu-item"

# Product Versions page
PRODUCT_VERSION_SAVE_BUTTON_XPATH = '//button[text()="Save"]'
NEW_PRODUCT_VERSION_TEXTBOX_ID = "new_version_name_text"
PRODUCT_VERSIONS_UL_CLASS_NAME = "pf-c-list"
PRODUCT_VERSIONS_LI_TAG_NAME = "li"
