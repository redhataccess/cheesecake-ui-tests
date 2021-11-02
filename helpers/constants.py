# Git import constants
git_import_branch="master"
# git_import_branch="noopur"
git_import_submitted_modal_title="Request submitted."
module_title_prefix = "Automated Title"
repo_url_empty_warning_message = "A repository url is required."
invalid_git_repo_url = "_)(*&^%$#@!"
repo_url_invalid_error_message = "Error cloning the repo due to invalid repo URL"
sort_by_upload_date = "Uploaded date"
failure_alert_message = "Git Import Failed"
success_alert_message = "Git Import Successful"
failure_alert_files_uploaded = "Total files uploaded: 0"
success_alert_files_uploaded = "Total files uploaded: "

# View module constants
path_to_module_to_be_published = "/uploader-sample-repo-pantheon2/entities/enterprise/modules/cockpit/con_pretty-host-name-in-the-web-console.adoc"
    # "repositories/rhel-8-docs-nmath-test/entities/enterprise/modules/upgrades-and-differences/ref_audit.adoc"
module_display_page_path_unpublished = "pantheon/#/module/repositories/uploader-sample-repo-pantheon2/entities/enterprise/modules/core-services/host-name.adoc?variant=variant1-uploader"
#"pantheon/#/repositories/rhel-8-docs-nmath-test/entities/enterprise/modules/upgrades-and-differences/ref_moved-packages.adoc"
module_display_page_path_published = "pantheon/#/module/repositories/uploader-sample-repo-pantheon2/entities/enterprise/modules/cockpit/proc_setting-the-host-name-using-the-web-console.adoc?variant=variant1-uploader"
    #"pantheon/#/repositories/rhel-8-docs-nmath-test/entities/enterprise/modules/upgrades-and-differences/ref_audit.adoc?variant=rhel83"
view_on_portal_link = "View on Customer Portal"
copy_url_link = "Copy permanent URL"
view_on_portal_page_url = "documentation/en-us/"


# Edit metadata constants
module_to_be_published = "at-uploader | Module Edit metadata Publish Title"
    # "Audit"
edit_metadata_modal_title = "Edit Metadata"
edit_metadata_modal_warning = "Fields indicated by * are mandatory"
product_version = "1"
use_case = "Install"
url_fragment = "test_url_fragment"
success_message = "Update Successful!"
default_use_case = "Select Use Case"
default_product_name = "Select a Product"
default_product_version = "Select a Version"

#constants for search modules
module_to_search = "AT via uploader | Pretty host name"
asian_char_module = "安装术语"
random_string_search = "abcdefg"
body_of_module_search = "search for body of the module"
no_module_found = "No modules found with your search"
help_user_guide_url = "/pantheon/docs/assemblies/assembly-pantheon-help.html"
bulk_operations_modules = "at-uploader | Module bulk operations"
bulk_operations_assemblies = "at-uploader | Assembly bulk operations"


# Create new product constants
new_product_name = "A Test Product RH_"
new_product_description = "Test Description"
blank_product_name_warning = "Fields indicated by * are mandatory"
duplicate_product_name_warning = "Duplicated Product name"
module_not_found = "Module not found"
version_url_fragment_warning = "Allowed input for ulrFragment: alphanumeric, hyphen, period and underscore"
new_product_url_fragment = "Test UrlFragment"
random = utilities.generate_random_string(4)
product_name = "AT Product Test" + random
product_name_uri = "at_product_test" + random


# Constants for future use
published_module = "at-uploader | Module Published Title"
# "Changes in core cryptographic components"
unpublished_module = "at-uploader | Module Unpublished Title and Module type test inside asciidoc Concept"
    # "Moved packages"
unpublished_module_preview_text = "Released content version not found for module"
delete_confirmation_modal_title = "Confirmation"
module_metadata_warning_title = "Module Versions"
module_metadata_warning = "Module failed to publish. Check the following:\nAre you logged in as a publisher?" \
                          "\nDoes the module have all required metadata?"

#constants for verifying attributes
search_module_with_attribute = "at-uploader | Assembly with attribute search"
attribute = "Red Hat Enterprise Linux 8"

# Module type constants
ref_module_title = "at-uploader | Module type test in filename Reference"
    # "New packages"
ref_module_title1 = "at-uploader | Module type test inside asciidoc Reference"
    # "OpenSCAP"
proc_module_title = "at-uploader | Module type test in filename Procedure"
# "Connecting to the web console from a remote machine"
proc_module_title1 = "at-uploader | Module type test inside asciidoc Procedure"
# "Installing the web console"
con_module_title = "at-uploader | Module type test in filename Concept"
    # "Pretty host name in the web console"
con_module_title1 = "at-uploader | Module Unpublished Title and Module type test inside asciidoc Concept"
    # "What is the RHEL web console"
no_module_type_title = "at-uploader | Module type none"
    # "What is the RHEL web console"
path_for_module_type = "/en_US/variants/variant1-uploader/draft/metadata/pant:moduleType.json"
    # "/en_US/variants/rhel83/draft/metadata"

# Create Product Versions
product_version_1 = "1"
product_version_2 = "alpha"
product_version_3 = "1.1"
product_version_url_fragment_1 = "product_version_urlFragment1"
product_version_url_fragment_2 = "product_version_urlFragment2"
product_version_url_fragment_3 = "product_version_urlFragment3"

# Assembly tests
assembly_to_be_published = "at-uploader | Assembly Publish test"
module_display_page_path_after_published = "pantheon/#/assembly/repositories/uploader-sample-repo-pantheon2/entities/enterprise/assemblies/assembly_configuring-the-host-name-in-the-web-console.adoc"
image_file_name = "cockpit-hostname-pf4.png"

legal_notice_link = "https://access.redhat.com/docs-legal-notice"

#search beta constants
no_results_found = "No results match the filter criteria. Select repo filter to show results."
publish_module = "at-uploader | Module type none"
error_for_multiple_repos_selected = "Please deselect all but one repository to continue."

# Constants for add new draft version test
module_new_draft_version = "at-uploader | Module new draft version test"
assembly_new_draft_version = "at-uploader | Assembly new draft version test"

#path for modules to unpublish
module_to_unpublish = "content/repositories/uploader-test/entities/enterprise/modules/cockpit/pretty-host-name-in-the-web-console.adoc"
assembly_to_unpublish = "content/repositories/uploader-test/entities/enterprise/assemblies/assembly_configuring-the-host-name-in-the-web-console.adoc"
view_module_unpubish = "content/repositories/uploader-test/entities/enterprise/modules/cockpit/setting-the-host-name-using-the-web-console.adoc"
proc_module_unpublish = "content/repositories/uploader-test/entities/enterprise/modules/installer/proc_adding-a-mount-point.adoc"
con_module_unpublish = "content/repositories/uploader-test/entities/enterprise/modules/installer/ref_installation-terminology.adoc"
ref_module_unpublish = "content/repositories/uploader-test/entities/enterprise/modules/installer/con_installation-options.adoc"
module_new_draft_unpublish = "/repositories/uploader-test/entities/enterprise/modules/core-kernel/new_draft_version.adoc"
assembly_new_draft_unpublish = "content/repositories/uploader-test/entities/enterprise/assemblies/assembly_new_draft_version.adoc"
search_module_unpublish = "content/repositories/uploader-test/entities/enterprise/modules/core-services/databases-intro.adoc"
variant = "variant1-uploader"

# Bulk operations constants
error_message_on_edit_metadata = "Danger alert:\nNo draft versions found on selected items. Unable to save metadata."

# xref validation constants
partial_title = "xref validation"
xref_validation_msg = "Invalid cross references"
xref_validation_module_name = "at-uploader | This doc contains a list of refs"
# xref validation constants in CP
Xref_linkText1 = "at-uploader | Assembly Publish test"
Xref_linkText2 = "Content Test Module | Logging in to the web console using Kerberos authentication (Image present)"
Xref_linkText3 = "at-uploader | Module type none"

Xref_dict = {"Xref_linkText1": "at-uploader | Assembly Publish test",
             "Xref_linkText2": "Content Test Module | Logging in to the web console using Kerberos authentication (Image present)",
             "Xref_linkText3": "at-uploader | Module type none"}
