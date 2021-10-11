# Common constants
WARNING_ALERT_CSS = "div.pf-c-alert.pf-m-warning h4.pf-c-alert__title"
WARNING_ALERT_DESCRIPTION_CSS = "div.pf-c-alert.pf-m-warning div.pf-c-alert__description"
CLOSE_WARNING_ALERT_CSS = "div.pf-c-alert__action button"

# Login page
LOGIN_LINK_TEXT = "Log In"
USER_NAME_ID = "username-verification"
LOGGED_IN_USERNAME = "a.p2-header__login"
PASSWORD_ID = "password"
LOGIN_NEXT_BUTTON_ID = "login-show-step2"
LOGIN_BUTTON_ID = "rh-password-verification-submit-button"
LOGGED_IN_USER_PARTIAL_TEXT = "Log Out"

# Display module page
MODULE_DISPLAY_TITLE_CSS = "div.pf-l-level h1"
MODULE_DISPLAY_PUBLISH_BUTTON_ID = "publishButton"
    # "button.pf-c-button.pf-m-primary"
MODULE_DISPLAY_UNPUBLISH_BUTTON_ID = "unpublishButton"
    # "button.pf-c-button.pf-m-primary"
MODULE_DISPLAY_PREVIEW_BUTTON_CSS = "div.pf-c-card__header div:nth-child(4) button"
MODULE_DISPLAY_FIRST_PUBLISHED_CSS = "div.pf-l-level:nth-child(5) div:nth-child(4) div.pf-c-content p:nth-child(1) > span:nth-child(3)"
MODULE_DISPLAY_LAST_PUBLISHED_CSS = "div.pf-l-level:nth-child(5) div:nth-child(5) div.pf-c-content p:nth-child(1) > span:nth-child(3)"
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
PRODUCT_INFO_CSS = "div.pf-l-level:nth-child(5) div:nth-child(1) div.pf-c-content p:nth-child(1) > span:nth-child(3)"
COPY_URL_LINK_CSS = "a#permanentURL"
VIEW_ON_PORTAL_LINK_CSS = "section.pf-c-page__main-section.pf-m-light div:nth-child(3) span:nth-child(1) a"
VIEW_MODULE_TYPE_CSS = "div.pf-l-level:nth-child(5) div:nth-child(3) div.pf-c-content p:nth-child(1) > span:nth-child(3)"
FIRST_PUB_DATE_MODULE_PAGE_CSS = "div.pf-l-level:nth-child(5) div:nth-child(4) div.pf-c-content p:nth-child(1) > span:nth-child(3)"
LAST_PUB_DATE_MODULE_PAGE_CSS = "div.pf-l-level:nth-child(5) div:nth-child(5) div.pf-c-content p:nth-child(1) > span:nth-child(3)"
MODULES_INCLUDED_LIST_CSS = "div.pf-c-content ul li a"
DRAFT_CARD = "article.pf-c-card-draft"
PUBLISHED_CARD = "article.pf-c-card.pf-m-selected"
UPLOAD_TIME_ON_DRAFT_CARD = "article.pf-c-card-draft div.pf-c-card__body div.pf-c-content:nth-child(1) p:nth-child(2)"
UPLOAD_TIME_ON_PUBLISHED_CARD = "article.pf-m-selected div.pf-c-card__body div.pf-c-content:nth-child(1) p:nth-child(2)"
DRAFT_CARD_TITLE = "article.pf-c-card-draft div.pf-c-card__header div strong"
PUBLISHED_CARD_TITLE = "article.pf-m-selected div.pf-c-card__header div strong span"
ATTRIBUTE_FILE_CSS = "div.pf-c-card__body div.pf-c-content:nth-child(3) p:nth-child(2)"
CARDS_ON_DETAILS_PAGE_CSS = "article.pf-c-card div div article.pf-c-card"
NO_URL_TOOLTIP_ICON = "div.pf-l-level:nth-child(3) div:nth-child(4) span div"
XREF_VALIDATION_TREE_ID = "xrefs"
XREF_VALIDATION_COUNT_CSS = "li#xrefs>div>button span.pf-c-badge.pf-m-read"
PATH_TO_ADOC_CSS = "div.pf-l-level>div>div.pf-c-content pre"
GENERATE_HTML_CSS = "button.pf-c-button.pf-m-secondary"

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
GIT_IMPORT_REQUEST_SUBMITTED_NO = "footer.pf-c-modal-box__footer button.pf-m-secondary"
REPO_URL_INVALID_ERROR_CSS = "div.pf-c-alert.pf-m-danger h4.pf-c-alert__title"
GIT_IMPORT_ALERT_CSS = "ul.pf-c-alert-group.git-import-alert-group.pf-m-toast li"
GIT_IMPORT_SUCCESS_ALERT_CSS = "div.pf-c-alert.pf-m-success"

# Search page
# FIRST_MODULE_CHECKBOX_XPATH = "//div[@id='data-rows'][2]/div[@class='pf-c-check checkbox']"
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
ALERT_TITLE_CSS = "h4.pf-c-alert__title"
CANCEL_BUTTON_XPATH = "//div[@class='pf-c-alert__action']/button"
SELECT_PRODUCT_NAME_CSS = "select#productForm"
SELECT_PRODUCT_VERSION_CSS = "select#productVersionForm"
PRODUCT_FILTER_DISPLAY_XPATH = "//div[@class='pf-c-chip-group pf-m-category']"
PRODUCT_VERSION_DISPLAY_PAGE_XPATH = "//div[@class='pf-l-level'][5]//div[1]/div/p/span"
SEARCH_RESULTS = "ul.pf-c-data-list"
MODULES_SELECT_ALL_TITLE_XPATH = "//table[@aria-label='Selectable Table module']/thead/tr/td/input[@name='check-all']"
ASSEMBLIES_SELECT_ALL_TITLE_XPATH = "//table[@aria-label='Selectable Table assembly']/thead/tr/td/input[@name='check-all']"
BULK_EDIT_METADATA_XPATH = "//button[@data-testid='edit_metadata']"
BULK_PUBLISH_CSS = "div.pf-c-toolbar__content-section div.pf-c-toolbar__item:nth-child(4) button"
BULK_UNPUBLISH_CSS = "div.pf-c-toolbar__content-section div.pf-c-toolbar__item:nth-child(5) button"
LIST_OF_MODULES_XPATH = "//table[@aria-label='Selectable Table module']/tbody/tr/th/div/a"
LIST_OF_ASSEMBLIES_XPATH = "//table[@aria-label='Selectable Table assembly']/tbody/tr/th/div/a"
EDIT_METADATA_MODAL_TITLE = "h1.pf-c-title.pf-m-2xl"
EDIT_METADATA_SELECT_PRODUCT = "//select[@aria-label='FormSelect Product']"
EDIT_METADATA_SELECT_VERSION = "//select[@aria-label='FormSelect Version']"
EDIT_METADATA_SELECT_USECASE = "//select[@aria-label='FormSelect Usecase']"
SELECTED_MODULES_COUNT_ID = "edit_metadata_helper_text"
EDIT_METADATA_SAVE = "//button[@form='bulk_edit_metadata']"
PROGRESS_SUCCESS_STATUS = "div.pf-m-success div:nth-child(2) span.pf-c-progress__measure"
VIEW_DETAILS_LINK = "//button[@data-testid='view-details-link']"
UPDATED_TITLES_LIST_CSS = "span#update-succeeded ol li"
FAILED_TITLES_LIST_CSS = "span#update-failed ul li"
SKIPPED_TITLE_LIST_CSS = "span#update-ignored ul li"
CLOSE_DETAILS_XPATH = "//button[@aria-label='Close']"
SKIPPED_TITLES_LIST_CSS = "span#update-ignored ol li"


#help_documentation_page
HELP_ICON_CLASS_NAME = "button.pf-c-dropdown__toggle.pf-m-plain"
USER_GUIDE_LINK_TEXT = "User Guide"
TITLE_OF_USER_GUIDE_CSS = "div.rhdocs__header__primary-wrapper h1"
USER_GUIDE_PARENT_CSS = "cp-documentation#doc-content"
GUIDE_TITLE="//div[@class='rhdocs-content-type']"
PAGE_DATA="help"

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
PUBLISHED_STATUS_CLASS_NAME = "dropdown-filter__option--published"
STATUS_TOOLBAR_CHIP_CLASS_NAME = "pf-m-chip-group"
SEARCH_TITLE_CSS = "#textInput span input"
TITLE_SEARCH_ICON_CSS = "button.pf-c-button.pf-m-control"
CONCEPT_CONTENT_TYPE_FILTER_CLASS_NAME = "dropdown-filter__option--concept"
PROCEDURE_CONTENT_TYPE_FILTER_CLASS_NAME = "dropdown-filter__option--procedure"
REFERENCE_CONTENT_TYPE_FILTER_CLASS_NAME = "dropdown-filter__option--reference"
FIRST_MODULE_LISTED_CSS = "div.search-results__section--module tbody tr:nth-child(1) th div a"
NTH_MODULE_LISTED_CSS = "div.search-results__section--module tbody tr:nth-child({}) th div a"
FIRST_LISTED_ASSEMBLY_CSS = "div.search-results__section--assembly tbody tr:nth-child(1) th div a"
FILTER_CHIP_LIST_CSS = "ul.pf-c-chip-group__list li div span"
ALL_MODULE_TITLES = "tbody tr th div a"
MODULES_LIST_CSS = "div.search-results__section--module div div table tbody tr th"
FIRST_MODULE_CHECKBOX_XPATH = "//table[@aria-label='Selectable Table module']//input[@name='checkrow0']"
MODAL_TITLE_CSS = "h1.pf-c-title"
TITLES_FOR_PUBLISH_CSS = "div#publish__module_helper_text"
TITLES_FOR_UNPUBLISH_CSS = "div#unpublish__module_helper_text"
CONFIRM_BUTTON_CSS = "footer.pf-c-modal-box__footer button.pf-c-button.pf-m-primary"
CLOSE_STATUS_ALERT = "div.pf-c-alert__action button.pf-c-button.pf-m-plain"
LIST_OF_REPOS_CSS = "div.repo-list-container ul li button div label"
LAST_PUBLISHED_DATE_XPATH = "//table[@aria-label='Selectable Table module']/tbody/tr/td[5]"
CLEAR_ALL_FILTER_CSS = "div#toolbar-with-filter div.pf-c-toolbar__content:nth-child(2) div.pf-c-toolbar__item:nth-child(2) button"
GREEN_CHECK_CLASS_NAME = "p2-search__check-circle-icon"
TITLES_ON_SEARCH_PAGE_XPATH = "//table[@aria-label='Selectable Table module']//th[2]"
REPOSITORY_ON_SEARCH_PAGE_XPATH = "//table[@aria-label='Selectable Table module']//th[3]"
UPLOAD_DATE_ON_SEARCH_PAGE_XPATH = "//table[@aria-label='Selectable Table module']//th[4]"
LAST_PUBLISHED_DATE_ON_SEARCH_PAGE_XPATH = "//table[@aria-label='Selectable Table module']//th[5]"
PAGINATION_ON_SEARCH_PAGE = "//button[@data-action='next']"
ERROR_FOR_MULTIPLE_REPO_SELECTED = "div.pf-c-alert__description"
SELECT_FIRST_REPO_XPATH = "//div[@aria-label='Repository List']//ul//li[1]//div//input"
SELECT_SECOND_REPO_XPATH = "//div[@aria-label='Repository List']//ul//li[2]//div//input"
CLEAR_REPO_FILTER_CSS = "div.filters-drawer__repo-search span.pf-c-search-input__clear"
XREF_VALIDATION_ICON_XPATH = "//td[@data-key='1']/div[2]/*[@fill='#c9190b']"
MODULE_SEARCH_RESULTS_CSS = "div.search-results__section--module tbody tr"