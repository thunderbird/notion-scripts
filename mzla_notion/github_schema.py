import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class ActorType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('TEAM', 'USER')


class AuditLogOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class Base64String(sgqlc.types.Scalar):
    __schema__ = schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = schema


Boolean = sgqlc.types.Boolean

class CheckAnnotationLevel(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FAILURE', 'NOTICE', 'WARNING')


class CheckConclusionState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTION_REQUIRED', 'CANCELLED', 'FAILURE', 'NEUTRAL', 'SKIPPED', 'STALE', 'STARTUP_FAILURE', 'SUCCESS', 'TIMED_OUT')


class CheckRunState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTION_REQUIRED', 'CANCELLED', 'COMPLETED', 'FAILURE', 'IN_PROGRESS', 'NEUTRAL', 'PENDING', 'QUEUED', 'SKIPPED', 'STALE', 'STARTUP_FAILURE', 'SUCCESS', 'TIMED_OUT', 'WAITING')


class CheckRunType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'LATEST')


class CheckStatusState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMPLETED', 'IN_PROGRESS', 'PENDING', 'QUEUED', 'REQUESTED', 'WAITING')


class CollaboratorAffiliation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'DIRECT', 'OUTSIDE')


class CommentAuthorAssociation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER')


class CommentCannotUpdateReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ARCHIVED', 'DENIED', 'INSUFFICIENT_ACCESS', 'LOCKED', 'LOGIN_REQUIRED', 'MAINTENANCE', 'VERIFIED_EMAIL_REQUIRED')


class CommitContributionOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMMIT_COUNT', 'OCCURRED_AT')


class ComparisonStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AHEAD', 'BEHIND', 'DIVERGED', 'IDENTICAL')


class ContributionLevel(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FIRST_QUARTILE', 'FOURTH_QUARTILE', 'NONE', 'SECOND_QUARTILE', 'THIRD_QUARTILE')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DefaultRepositoryPermissionField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'NONE', 'READ', 'WRITE')


class DependencyGraphEcosystem(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTIONS', 'COMPOSER', 'GO', 'MAVEN', 'NPM', 'NUGET', 'PIP', 'PUB', 'RUBYGEMS', 'RUST', 'SWIFT')


class DeploymentOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class DeploymentProtectionRuleType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BRANCH_POLICY', 'REQUIRED_REVIEWERS', 'WAIT_TIMER')


class DeploymentReviewState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('APPROVED', 'REJECTED')


class DeploymentState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ABANDONED', 'ACTIVE', 'DESTROYED', 'ERROR', 'FAILURE', 'INACTIVE', 'IN_PROGRESS', 'PENDING', 'QUEUED', 'SUCCESS', 'WAITING')


class DeploymentStatusState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ERROR', 'FAILURE', 'INACTIVE', 'IN_PROGRESS', 'PENDING', 'QUEUED', 'SUCCESS', 'WAITING')


class DiffSide(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LEFT', 'RIGHT')


class DiscussionCloseReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DUPLICATE', 'OUTDATED', 'RESOLVED')


class DiscussionOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT')


class DiscussionPollOptionOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AUTHORED_ORDER', 'VOTE_COUNT')


class DiscussionState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class DiscussionStateReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DUPLICATE', 'OUTDATED', 'REOPENED', 'RESOLVED')


class DismissReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FIX_STARTED', 'INACCURATE', 'NOT_USED', 'NO_BANDWIDTH', 'TOLERABLE_RISK')


class EnterpriseAdministratorInvitationOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class EnterpriseAdministratorRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BILLING_MANAGER', 'OWNER', 'UNAFFILIATED')


class EnterpriseAllowPrivateRepositoryForkingPolicyValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ENTERPRISE_ORGANIZATIONS', 'ENTERPRISE_ORGANIZATIONS_USER_ACCOUNTS', 'EVERYWHERE', 'SAME_ORGANIZATION', 'SAME_ORGANIZATION_USER_ACCOUNTS', 'USER_ACCOUNTS')


class EnterpriseDefaultRepositoryPermissionSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'NONE', 'NO_POLICY', 'READ', 'WRITE')


class EnterpriseDisallowedMethodsSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INSECURE', 'NO_POLICY')


class EnterpriseEnabledDisabledSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'ENABLED', 'NO_POLICY')


class EnterpriseEnabledSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ENABLED', 'NO_POLICY')


class EnterpriseMemberInvitationOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class EnterpriseMemberOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'LOGIN')


class EnterpriseMembersCanCreateRepositoriesSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'DISABLED', 'NO_POLICY', 'PRIVATE', 'PUBLIC')


class EnterpriseMembersCanMakePurchasesSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'ENABLED')


class EnterpriseMembershipType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'ALL', 'BILLING_MANAGER', 'ORG_MEMBERSHIP')


class EnterpriseOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NAME',)


class EnterpriseServerInstallationOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'CUSTOMER_NAME', 'HOST_NAME')


class EnterpriseServerUserAccountEmailOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('EMAIL',)


class EnterpriseServerUserAccountOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LOGIN', 'REMOTE_CREATED_AT')


class EnterpriseServerUserAccountsUploadOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class EnterpriseServerUserAccountsUploadSyncState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FAILURE', 'PENDING', 'SUCCESS')


class EnterpriseUserAccountMembershipRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MEMBER', 'OWNER', 'UNAFFILIATED')


class EnterpriseUserDeployment(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOUD', 'SERVER')


class EnvironmentOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NAME',)


class EnvironmentPinnedFilterField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'NONE', 'ONLY')


class FileViewedState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISMISSED', 'UNVIEWED', 'VIEWED')


Float = sgqlc.types.Float

class FundingPlatform(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BUY_ME_A_COFFEE', 'COMMUNITY_BRIDGE', 'CUSTOM', 'GITHUB', 'ISSUEHUNT', 'KO_FI', 'LFX_CROWDFUNDING', 'LIBERAPAY', 'OPEN_COLLECTIVE', 'PATREON', 'POLAR', 'THANKS_DEV', 'TIDELIFT')


class GistOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'PUSHED_AT', 'UPDATED_AT')


class GistPrivacy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'PUBLIC', 'SECRET')


class GitObjectID(sgqlc.types.Scalar):
    __schema__ = schema


class GitRefname(sgqlc.types.Scalar):
    __schema__ = schema


class GitSSHRemote(sgqlc.types.Scalar):
    __schema__ = schema


class GitSignatureState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BAD_CERT', 'BAD_EMAIL', 'EXPIRED_KEY', 'GPGVERIFY_ERROR', 'GPGVERIFY_UNAVAILABLE', 'INVALID', 'MALFORMED_SIG', 'NOT_SIGNING_KEY', 'NO_USER', 'OCSP_ERROR', 'OCSP_PENDING', 'OCSP_REVOKED', 'UNKNOWN_KEY', 'UNKNOWN_SIG_TYPE', 'UNSIGNED', 'UNVERIFIED_EMAIL', 'VALID')


class GitTimestamp(sgqlc.types.Scalar):
    __schema__ = schema


class HTML(sgqlc.types.Scalar):
    __schema__ = schema


ID = sgqlc.types.ID

class IdentityProviderConfigurationState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONFIGURED', 'ENFORCED', 'UNCONFIGURED')


Int = sgqlc.types.Int

class IpAllowListEnabledSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'ENABLED')


class IpAllowListEntryOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALLOW_LIST_VALUE', 'CREATED_AT')


class IpAllowListForInstalledAppsEnabledSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'ENABLED')


class IssueClosedStateReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMPLETED', 'DUPLICATE', 'NOT_PLANNED')


class IssueCommentOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('UPDATED_AT',)


class IssueDependencyOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'DEPENDENCY_ADDED_AT')


class IssueOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMMENTS', 'CREATED_AT', 'UPDATED_AT')


class IssueState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class IssueStateReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMPLETED', 'DUPLICATE', 'NOT_PLANNED', 'REOPENED')


class IssueTimelineItemsItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADDED_TO_PROJECT_EVENT', 'ADDED_TO_PROJECT_V2_EVENT', 'ASSIGNED_EVENT', 'BLOCKED_BY_ADDED_EVENT', 'BLOCKED_BY_REMOVED_EVENT', 'BLOCKING_ADDED_EVENT', 'BLOCKING_REMOVED_EVENT', 'CLOSED_EVENT', 'COMMENT_DELETED_EVENT', 'CONNECTED_EVENT', 'CONVERTED_FROM_DRAFT_EVENT', 'CONVERTED_NOTE_TO_ISSUE_EVENT', 'CONVERTED_TO_DISCUSSION_EVENT', 'CROSS_REFERENCED_EVENT', 'DEMILESTONED_EVENT', 'DISCONNECTED_EVENT', 'ISSUE_COMMENT', 'ISSUE_TYPE_ADDED_EVENT', 'ISSUE_TYPE_CHANGED_EVENT', 'ISSUE_TYPE_REMOVED_EVENT', 'LABELED_EVENT', 'LOCKED_EVENT', 'MARKED_AS_DUPLICATE_EVENT', 'MENTIONED_EVENT', 'MILESTONED_EVENT', 'MOVED_COLUMNS_IN_PROJECT_EVENT', 'PARENT_ISSUE_ADDED_EVENT', 'PARENT_ISSUE_REMOVED_EVENT', 'PINNED_EVENT', 'PROJECT_V2_ITEM_STATUS_CHANGED_EVENT', 'REFERENCED_EVENT', 'REMOVED_FROM_PROJECT_EVENT', 'REMOVED_FROM_PROJECT_V2_EVENT', 'RENAMED_TITLE_EVENT', 'REOPENED_EVENT', 'SUBSCRIBED_EVENT', 'SUB_ISSUE_ADDED_EVENT', 'SUB_ISSUE_REMOVED_EVENT', 'TRANSFERRED_EVENT', 'UNASSIGNED_EVENT', 'UNLABELED_EVENT', 'UNLOCKED_EVENT', 'UNMARKED_AS_DUPLICATE_EVENT', 'UNPINNED_EVENT', 'UNSUBSCRIBED_EVENT', 'USER_BLOCKED_EVENT')


class IssueTypeColor(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLUE', 'GRAY', 'GREEN', 'ORANGE', 'PINK', 'PURPLE', 'RED', 'YELLOW')


class IssueTypeOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME')


class LabelOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'ISSUE_COUNT', 'NAME')


class LanguageOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SIZE',)


class LockReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('OFF_TOPIC', 'RESOLVED', 'SPAM', 'TOO_HEATED')


class MannequinOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'LOGIN')


class MergeCommitMessage(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLANK', 'PR_BODY', 'PR_TITLE')


class MergeCommitTitle(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MERGE_MESSAGE', 'PR_TITLE')


class MergeQueueEntryState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AWAITING_CHECKS', 'LOCKED', 'MERGEABLE', 'QUEUED', 'UNMERGEABLE')


class MergeQueueGroupingStrategy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALLGREEN', 'HEADGREEN')


class MergeQueueMergeMethod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MERGE', 'REBASE', 'SQUASH')


class MergeQueueMergingStrategy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALLGREEN', 'HEADGREEN')


class MergeStateStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BEHIND', 'BLOCKED', 'CLEAN', 'DIRTY', 'HAS_HOOKS', 'UNKNOWN', 'UNSTABLE')


class MergeableState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONFLICTING', 'MERGEABLE', 'UNKNOWN')


class MigrationSourceType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AZURE_DEVOPS', 'BITBUCKET_SERVER', 'GITHUB_ARCHIVE')


class MigrationState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FAILED', 'FAILED_VALIDATION', 'IN_PROGRESS', 'NOT_STARTED', 'PENDING_VALIDATION', 'QUEUED', 'SUCCEEDED')


class MilestoneOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'DUE_DATE', 'NUMBER', 'UPDATED_AT')


class MilestoneState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class NotificationRestrictionSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'ENABLED')


class OIDCProviderType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AAD',)


class OauthApplicationCreateAuditEntryState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTIVE', 'PENDING_DELETION', 'SUSPENDED')


class OperationType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACCESS', 'AUTHENTICATION', 'CREATE', 'MODIFY', 'REMOVE', 'RESTORE', 'TRANSFER')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ASC', 'DESC')


class OrgAddMemberAuditEntryPermission(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'READ')


class OrgCreateAuditEntryBillingPlan(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BUSINESS', 'BUSINESS_PLUS', 'FREE', 'TIERED_PER_SEAT', 'UNLIMITED')


class OrgEnterpriseOwnerOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LOGIN',)


class OrgRemoveBillingManagerAuditEntryReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SAML_EXTERNAL_IDENTITY_MISSING', 'SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY', 'TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE')


class OrgRemoveMemberAuditEntryMembershipType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'BILLING_MANAGER', 'DIRECT_MEMBER', 'OUTSIDE_COLLABORATOR', 'SUSPENDED', 'UNAFFILIATED')


class OrgRemoveMemberAuditEntryReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SAML_EXTERNAL_IDENTITY_MISSING', 'SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY', 'TWO_FACTOR_ACCOUNT_RECOVERY', 'TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE', 'USER_ACCOUNT_DELETED')


class OrgRemoveOutsideCollaboratorAuditEntryMembershipType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BILLING_MANAGER', 'OUTSIDE_COLLABORATOR', 'UNAFFILIATED')


class OrgRemoveOutsideCollaboratorAuditEntryReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SAML_EXTERNAL_IDENTITY_MISSING', 'TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE')


class OrgUpdateDefaultRepositoryPermissionAuditEntryPermission(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'NONE', 'READ', 'WRITE')


class OrgUpdateMemberAuditEntryPermission(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'READ')


class OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'INTERNAL', 'NONE', 'PRIVATE', 'PRIVATE_INTERNAL', 'PUBLIC', 'PUBLIC_INTERNAL', 'PUBLIC_PRIVATE')


class OrganizationInvitationRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'BILLING_MANAGER', 'DIRECT_MEMBER', 'REINSTATE')


class OrganizationInvitationSource(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MEMBER', 'SCIM', 'UNKNOWN')


class OrganizationInvitationType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('EMAIL', 'USER')


class OrganizationMemberRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'MEMBER')


class OrganizationMembersCanCreateRepositoriesSettingValue(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'DISABLED', 'INTERNAL', 'PRIVATE')


class OrganizationMigrationState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FAILED', 'FAILED_VALIDATION', 'IN_PROGRESS', 'NOT_STARTED', 'PENDING_VALIDATION', 'POST_REPO_MIGRATION', 'PRE_REPO_MIGRATION', 'QUEUED', 'REPO_MIGRATION', 'SUCCEEDED')


class OrganizationOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'LOGIN')


class PackageFileOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class PackageOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class PackageType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DEBIAN', 'PYPI')


class PackageVersionOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class PatchStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADDED', 'CHANGED', 'COPIED', 'DELETED', 'MODIFIED', 'RENAMED')


class PinnableItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('GIST', 'ISSUE', 'ORGANIZATION', 'PROJECT', 'PULL_REQUEST', 'REPOSITORY', 'TEAM', 'USER')


class PinnedDiscussionGradient(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLUE_MINT', 'BLUE_PURPLE', 'PINK_BLUE', 'PURPLE_CORAL', 'RED_ORANGE')


class PinnedDiscussionPattern(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CHEVRON_UP', 'DOT', 'DOT_FILL', 'HEART_FILL', 'PLUS', 'ZAP')


class PinnedEnvironmentOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('POSITION',)


class PreciseDateTime(sgqlc.types.Scalar):
    __schema__ = schema


class ProjectCardArchivedState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ()


class ProjectCardState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONTENT_ONLY', 'NOTE_ONLY', 'REDACTED')


class ProjectColumnPurpose(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DONE', 'IN_PROGRESS', 'TODO')


class ProjectOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME', 'UPDATED_AT')


class ProjectState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class ProjectTemplate(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AUTOMATED_KANBAN_V2', 'AUTOMATED_REVIEWS_KANBAN', 'BASIC_KANBAN', 'BUG_TRIAGE')


class ProjectV2CustomFieldType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATE', 'ITERATION', 'NUMBER', 'SINGLE_SELECT', 'TEXT')


class ProjectV2FieldOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME', 'POSITION')


class ProjectV2FieldType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ASSIGNEES', 'DATE', 'ISSUE_TYPE', 'ITERATION', 'LABELS', 'LINKED_PULL_REQUESTS', 'MILESTONE', 'NUMBER', 'PARENT_ISSUE', 'REPOSITORY', 'REVIEWERS', 'SINGLE_SELECT', 'SUB_ISSUES_PROGRESS', 'TEXT', 'TITLE', 'TRACKED_BY', 'TRACKS')


class ProjectV2ItemFieldValueOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('POSITION',)


class ProjectV2ItemOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('POSITION',)


class ProjectV2ItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DRAFT_ISSUE', 'ISSUE', 'PULL_REQUEST', 'REDACTED')


class ProjectV2OrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NUMBER', 'TITLE', 'UPDATED_AT')


class ProjectV2PermissionLevel(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'READ', 'WRITE')


class ProjectV2Roles(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'NONE', 'READER', 'WRITER')


class ProjectV2SingleSelectFieldOptionColor(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLUE', 'GRAY', 'GREEN', 'ORANGE', 'PINK', 'PURPLE', 'RED', 'YELLOW')


class ProjectV2State(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class ProjectV2StatusUpdateOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class ProjectV2StatusUpdateStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AT_RISK', 'COMPLETE', 'INACTIVE', 'OFF_TRACK', 'ON_TRACK')


class ProjectV2ViewLayout(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BOARD_LAYOUT', 'ROADMAP_LAYOUT', 'TABLE_LAYOUT')


class ProjectV2ViewOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME', 'POSITION')


class ProjectV2WorkflowsOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME', 'NUMBER', 'UPDATED_AT')


class PullRequestAllowedMergeMethods(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MERGE', 'REBASE', 'SQUASH')


class PullRequestBranchUpdateMethod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MERGE', 'REBASE')


class PullRequestMergeMethod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MERGE', 'REBASE', 'SQUASH')


class PullRequestOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT')


class PullRequestReviewCommentState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('PENDING', 'SUBMITTED')


class PullRequestReviewDecision(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('APPROVED', 'CHANGES_REQUESTED', 'REVIEW_REQUIRED')


class PullRequestReviewEvent(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('APPROVE', 'COMMENT', 'DISMISS', 'REQUEST_CHANGES')


class PullRequestReviewState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('APPROVED', 'CHANGES_REQUESTED', 'COMMENTED', 'DISMISSED', 'PENDING')


class PullRequestReviewThreadSubjectType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FILE', 'LINE')


class PullRequestState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'MERGED', 'OPEN')


class PullRequestTimelineItemsItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADDED_TO_MERGE_QUEUE_EVENT', 'ADDED_TO_PROJECT_EVENT', 'ADDED_TO_PROJECT_V2_EVENT', 'ASSIGNED_EVENT', 'AUTOMATIC_BASE_CHANGE_FAILED_EVENT', 'AUTOMATIC_BASE_CHANGE_SUCCEEDED_EVENT', 'AUTO_MERGE_DISABLED_EVENT', 'AUTO_MERGE_ENABLED_EVENT', 'AUTO_REBASE_ENABLED_EVENT', 'AUTO_SQUASH_ENABLED_EVENT', 'BASE_REF_CHANGED_EVENT', 'BASE_REF_DELETED_EVENT', 'BASE_REF_FORCE_PUSHED_EVENT', 'BLOCKED_BY_ADDED_EVENT', 'BLOCKED_BY_REMOVED_EVENT', 'BLOCKING_ADDED_EVENT', 'BLOCKING_REMOVED_EVENT', 'CLOSED_EVENT', 'COMMENT_DELETED_EVENT', 'CONNECTED_EVENT', 'CONVERTED_FROM_DRAFT_EVENT', 'CONVERTED_NOTE_TO_ISSUE_EVENT', 'CONVERTED_TO_DISCUSSION_EVENT', 'CONVERT_TO_DRAFT_EVENT', 'CROSS_REFERENCED_EVENT', 'DEMILESTONED_EVENT', 'DEPLOYED_EVENT', 'DEPLOYMENT_ENVIRONMENT_CHANGED_EVENT', 'DISCONNECTED_EVENT', 'HEAD_REF_DELETED_EVENT', 'HEAD_REF_FORCE_PUSHED_EVENT', 'HEAD_REF_RESTORED_EVENT', 'ISSUE_COMMENT', 'ISSUE_TYPE_ADDED_EVENT', 'ISSUE_TYPE_CHANGED_EVENT', 'ISSUE_TYPE_REMOVED_EVENT', 'LABELED_EVENT', 'LOCKED_EVENT', 'MARKED_AS_DUPLICATE_EVENT', 'MENTIONED_EVENT', 'MERGED_EVENT', 'MILESTONED_EVENT', 'MOVED_COLUMNS_IN_PROJECT_EVENT', 'PARENT_ISSUE_ADDED_EVENT', 'PARENT_ISSUE_REMOVED_EVENT', 'PINNED_EVENT', 'PROJECT_V2_ITEM_STATUS_CHANGED_EVENT', 'PULL_REQUEST_COMMIT', 'PULL_REQUEST_COMMIT_COMMENT_THREAD', 'PULL_REQUEST_REVIEW', 'PULL_REQUEST_REVIEW_THREAD', 'PULL_REQUEST_REVISION_MARKER', 'READY_FOR_REVIEW_EVENT', 'REFERENCED_EVENT', 'REMOVED_FROM_MERGE_QUEUE_EVENT', 'REMOVED_FROM_PROJECT_EVENT', 'REMOVED_FROM_PROJECT_V2_EVENT', 'RENAMED_TITLE_EVENT', 'REOPENED_EVENT', 'REVIEW_DISMISSED_EVENT', 'REVIEW_REQUESTED_EVENT', 'REVIEW_REQUEST_REMOVED_EVENT', 'SUBSCRIBED_EVENT', 'SUB_ISSUE_ADDED_EVENT', 'SUB_ISSUE_REMOVED_EVENT', 'TRANSFERRED_EVENT', 'UNASSIGNED_EVENT', 'UNLABELED_EVENT', 'UNLOCKED_EVENT', 'UNMARKED_AS_DUPLICATE_EVENT', 'UNPINNED_EVENT', 'UNSUBSCRIBED_EVENT', 'USER_BLOCKED_EVENT')


class PullRequestUpdateState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class ReactionContent(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CONFUSED', 'EYES', 'HEART', 'HOORAY', 'LAUGH', 'ROCKET', 'THUMBS_DOWN', 'THUMBS_UP')


class ReactionOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class RefOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALPHABETICAL', 'TAG_COMMIT_DATE')


class ReleaseOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME')


class RepoAccessAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoAddMemberAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoArchivedAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoChangeMergeSettingAuditEntryMergeType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MERGE', 'REBASE', 'SQUASH')


class RepoCreateAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoDestroyAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoRemoveMemberAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class ReportedContentClassifiers(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ABUSE', 'DUPLICATE', 'OFF_TOPIC', 'OUTDATED', 'RESOLVED', 'SPAM')


class RepositoryAffiliation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COLLABORATOR', 'ORGANIZATION_MEMBER', 'OWNER')


class RepositoryContributionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMMIT', 'ISSUE', 'PULL_REQUEST', 'PULL_REQUEST_REVIEW', 'REPOSITORY')


class RepositoryInteractionLimit(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COLLABORATORS_ONLY', 'CONTRIBUTORS_ONLY', 'EXISTING_USERS', 'NO_LIMIT')


class RepositoryInteractionLimitExpiry(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ONE_DAY', 'ONE_MONTH', 'ONE_WEEK', 'SIX_MONTHS', 'THREE_DAYS')


class RepositoryInteractionLimitOrigin(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ORGANIZATION', 'REPOSITORY', 'USER')


class RepositoryInvitationOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class RepositoryLockReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BILLING', 'MIGRATING', 'MOVING', 'RENAME', 'TRADE_RESTRICTION', 'TRANSFERRING_OWNERSHIP')


class RepositoryMigrationOrderDirection(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ASC', 'DESC')


class RepositoryMigrationOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class RepositoryOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME', 'PUSHED_AT', 'STARGAZERS', 'UPDATED_AT')


class RepositoryPermission(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'MAINTAIN', 'READ', 'TRIAGE', 'WRITE')


class RepositoryPrivacy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('PRIVATE', 'PUBLIC')


class RepositoryRuleOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'TYPE', 'UPDATED_AT')


class RepositoryRuleType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AUTHORIZATION', 'BRANCH_NAME_PATTERN', 'CODE_SCANNING', 'COMMITTER_EMAIL_PATTERN', 'COMMIT_AUTHOR_EMAIL_PATTERN', 'COMMIT_MESSAGE_PATTERN', 'COPILOT_CODE_REVIEW', 'CREATION', 'DELETION', 'FILE_EXTENSION_RESTRICTION', 'FILE_PATH_RESTRICTION', 'LOCK_BRANCH', 'MAX_FILE_PATH_LENGTH', 'MAX_FILE_SIZE', 'MAX_REF_UPDATES', 'MERGE_QUEUE', 'MERGE_QUEUE_LOCKED_REF', 'NON_FAST_FORWARD', 'PULL_REQUEST', 'REQUIRED_DEPLOYMENTS', 'REQUIRED_LINEAR_HISTORY', 'REQUIRED_REVIEW_THREAD_RESOLUTION', 'REQUIRED_SIGNATURES', 'REQUIRED_STATUS_CHECKS', 'REQUIRED_WORKFLOW_STATUS_CHECKS', 'SECRET_SCANNING', 'TAG', 'TAG_NAME_PATTERN', 'UPDATE', 'WORKFLOWS', 'WORKFLOW_UPDATES')


class RepositoryRulesetBypassActorBypassMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALWAYS', 'EXEMPT', 'PULL_REQUEST')


class RepositoryRulesetTarget(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BRANCH', 'PUSH', 'REPOSITORY', 'TAG')


class RepositorySuggestedActorFilter(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CAN_BE_ASSIGNED', 'CAN_BE_AUTHOR')


class RepositoryVisibility(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepositoryVulnerabilityAlertDependencyRelationship(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DIRECT', 'INCONCLUSIVE', 'TRANSITIVE', 'UNKNOWN')


class RepositoryVulnerabilityAlertDependencyScope(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DEVELOPMENT', 'RUNTIME')


class RepositoryVulnerabilityAlertState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AUTO_DISMISSED', 'DISMISSED', 'FIXED', 'OPEN')


class RequestableCheckStatusState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMPLETED', 'IN_PROGRESS', 'PENDING', 'QUEUED', 'WAITING')


class RoleInOrganization(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DIRECT_MEMBER', 'OWNER', 'UNAFFILIATED')


class RuleEnforcement(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTIVE', 'DISABLED', 'EVALUATE')


class SamlDigestAlgorithm(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SHA1', 'SHA256', 'SHA384', 'SHA512')


class SamlSignatureAlgorithm(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('RSA_SHA1', 'RSA_SHA256', 'RSA_SHA384', 'RSA_SHA512')


class SavedReplyOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('UPDATED_AT',)


class SearchType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISCUSSION', 'ISSUE', 'ISSUE_ADVANCED', 'REPOSITORY', 'USER')


class SecurityAdvisoryClassification(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('GENERAL', 'MALWARE')


class SecurityAdvisoryEcosystem(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTIONS', 'COMPOSER', 'ERLANG', 'GO', 'MAVEN', 'NPM', 'NUGET', 'PIP', 'PUB', 'RUBYGEMS', 'RUST', 'SWIFT')


class SecurityAdvisoryIdentifierType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CVE', 'GHSA')


class SecurityAdvisoryOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('EPSS_PERCENTAGE', 'EPSS_PERCENTILE', 'PUBLISHED_AT', 'UPDATED_AT')


class SecurityAdvisorySeverity(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CRITICAL', 'HIGH', 'LOW', 'MODERATE')


class SecurityVulnerabilityOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('UPDATED_AT',)


class SocialAccountProvider(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLUESKY', 'FACEBOOK', 'GENERIC', 'HOMETOWN', 'INSTAGRAM', 'LINKEDIN', 'MASTODON', 'NPM', 'REDDIT', 'TWITCH', 'TWITTER', 'YOUTUBE')


class SponsorAndLifetimeValueOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LIFETIME_VALUE', 'SPONSOR_LOGIN', 'SPONSOR_RELEVANCE')


class SponsorOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LOGIN', 'RELEVANCE')


class SponsorableOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LOGIN',)


class SponsorsActivityAction(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CANCELLED_SPONSORSHIP', 'NEW_SPONSORSHIP', 'PENDING_CHANGE', 'REFUND', 'SPONSOR_MATCH_DISABLED', 'TIER_CHANGE')


class SponsorsActivityOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('TIMESTAMP',)


class SponsorsActivityPeriod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'DAY', 'MONTH', 'WEEK')


class SponsorsCountryOrRegionCode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW')


class SponsorsGoalKind(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MONTHLY_SPONSORSHIP_AMOUNT', 'TOTAL_SPONSORS_COUNT')


class SponsorsListingFeaturedItemFeatureableType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('REPOSITORY', 'USER')


class SponsorsTierOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'MONTHLY_PRICE_IN_CENTS')


class SponsorshipNewsletterOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class SponsorshipOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class SponsorshipPaymentSource(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('GITHUB', 'PATREON')


class SponsorshipPrivacy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('PRIVATE', 'PUBLIC')


class SquashMergeCommitMessage(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('BLANK', 'COMMIT_MESSAGES', 'PR_BODY')


class SquashMergeCommitTitle(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMMIT_OR_PR_TITLE', 'PR_TITLE')


class StarOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('STARRED_AT',)


class StatusState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ERROR', 'EXPECTED', 'FAILURE', 'PENDING', 'SUCCESS')


String = sgqlc.types.String

class SubscriptionState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IGNORED', 'SUBSCRIBED', 'UNSUBSCRIBED')


class TeamDiscussionCommentOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NUMBER',)


class TeamDiscussionOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class TeamMemberOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'LOGIN')


class TeamMemberRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MAINTAINER', 'MEMBER')


class TeamMembershipType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ALL', 'CHILD_TEAM', 'IMMEDIATE')


class TeamNotificationSetting(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NOTIFICATIONS_DISABLED', 'NOTIFICATIONS_ENABLED')


class TeamOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NAME',)


class TeamPrivacy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('SECRET', 'VISIBLE')


class TeamRepositoryOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'NAME', 'PERMISSION', 'PUSHED_AT', 'STARGAZERS', 'UPDATED_AT')


class TeamReviewAssignmentAlgorithm(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LOAD_BALANCE', 'ROUND_ROBIN')


class TeamRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'MEMBER')


class ThreadSubscriptionFormAction(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NONE', 'SUBSCRIBE', 'UNSUBSCRIBE')


class ThreadSubscriptionState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'IGNORING_LIST', 'IGNORING_THREAD', 'NONE', 'SUBSCRIBED_TO_LIST', 'SUBSCRIBED_TO_THREAD', 'SUBSCRIBED_TO_THREAD_EVENTS', 'SUBSCRIBED_TO_THREAD_TYPE', 'UNAVAILABLE')


class TopicSuggestionDeclineReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ()


class TrackedIssueStates(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CLOSED', 'OPEN')


class TwoFactorCredentialSecurityType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISABLED', 'INSECURE', 'SECURE')


class URI(sgqlc.types.Scalar):
    __schema__ = schema


class UserBlockDuration(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ONE_DAY', 'ONE_MONTH', 'ONE_WEEK', 'PERMANENT', 'THREE_DAYS')


class UserStatusOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('UPDATED_AT',)


class UserViewType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('PRIVATE', 'PUBLIC')


class VerifiableDomainOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT', 'DOMAIN')


class WorkflowRunOrderField(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT',)


class WorkflowState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTIVE', 'DELETED', 'DISABLED_FORK', 'DISABLED_INACTIVITY', 'DISABLED_MANUALLY')


class X509Certificate(sgqlc.types.Scalar):
    __schema__ = schema



########################################################################
# Input Objects
########################################################################
class AbortQueuedMigrationsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')


class AbortRepositoryMigrationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'migration_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    migration_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='migrationId')


class AcceptEnterpriseAdministratorInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='invitationId')


class AcceptEnterpriseMemberInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='invitationId')


class AcceptTopicSuggestionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    name = sgqlc.types.Field(String, graphql_name='name')


class AccessUserNamespaceRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class AddAssigneesToAssignableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'assignable_id', 'assignee_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    assignable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='assignableId')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')


class AddBlockedByInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'blocking_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    blocking_issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='blockingIssueId')


class AddCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class AddDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion_id', 'reply_to_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='discussionId')
    reply_to_id = sgqlc.types.Field(ID, graphql_name='replyToId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class AddDiscussionPollVoteInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'poll_option_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    poll_option_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pollOptionId')


class AddEnterpriseOrganizationMemberInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'organization_id', 'user_ids', 'role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userIds')
    role = sgqlc.types.Field(OrganizationMemberRole, graphql_name='role')


class AddEnterpriseSupportEntitlementInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')


class AddLabelsToLabelableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'labelable_id', 'label_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='labelableId')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='labelIds')


class AddProjectCardInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_column_id', 'content_id', 'note')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectColumnId')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    note = sgqlc.types.Field(String, graphql_name='note')


class AddProjectColumnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class AddProjectV2DraftIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'title', 'body', 'assignee_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')


class AddProjectV2ItemByIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'content_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    content_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='contentId')


class AddPullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'pull_request_review_id', 'commit_oid', 'body', 'path', 'position', 'in_reply_to')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(ID, graphql_name='pullRequestId')
    pull_request_review_id = sgqlc.types.Field(ID, graphql_name='pullRequestReviewId')
    commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='commitOID')
    body = sgqlc.types.Field(String, graphql_name='body')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    in_reply_to = sgqlc.types.Field(ID, graphql_name='inReplyTo')


class AddPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'commit_oid', 'body', 'event', 'comments', 'threads')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='commitOID')
    body = sgqlc.types.Field(String, graphql_name='body')
    event = sgqlc.types.Field(PullRequestReviewEvent, graphql_name='event')
    comments = sgqlc.types.Field(sgqlc.types.list_of('DraftPullRequestReviewComment'), graphql_name='comments')
    threads = sgqlc.types.Field(sgqlc.types.list_of('DraftPullRequestReviewThread'), graphql_name='threads')


class AddPullRequestReviewThreadInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'path', 'body', 'pull_request_id', 'pull_request_review_id', 'line', 'side', 'start_line', 'start_side', 'subject_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    path = sgqlc.types.Field(String, graphql_name='path')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    pull_request_id = sgqlc.types.Field(ID, graphql_name='pullRequestId')
    pull_request_review_id = sgqlc.types.Field(ID, graphql_name='pullRequestReviewId')
    line = sgqlc.types.Field(Int, graphql_name='line')
    side = sgqlc.types.Field(DiffSide, graphql_name='side')
    start_line = sgqlc.types.Field(Int, graphql_name='startLine')
    start_side = sgqlc.types.Field(DiffSide, graphql_name='startSide')
    subject_type = sgqlc.types.Field(PullRequestReviewThreadSubjectType, graphql_name='subjectType')


class AddPullRequestReviewThreadReplyInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review_id', 'pull_request_review_thread_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(ID, graphql_name='pullRequestReviewId')
    pull_request_review_thread_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewThreadId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class AddReactionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id', 'content')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')


class AddStarInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'starrable_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='starrableId')


class AddSubIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'sub_issue_id', 'sub_issue_url', 'replace_parent')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    sub_issue_id = sgqlc.types.Field(ID, graphql_name='subIssueId')
    sub_issue_url = sgqlc.types.Field(String, graphql_name='subIssueUrl')
    replace_parent = sgqlc.types.Field(Boolean, graphql_name='replaceParent')


class AddUpvoteInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')


class AddVerifiableDomainInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'domain')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    domain = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='domain')


class ApproveDeploymentsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'workflow_run_id', 'environment_ids', 'comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workflow_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workflowRunId')
    environment_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='environmentIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class ApproveVerifiableDomainInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ArchiveProjectV2ItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'item_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')


class ArchiveRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class AuditLogOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(AuditLogOrderField, graphql_name='field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')


class BranchNamePatternParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(Boolean, graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class BulkSponsorship(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('sponsorable_id', 'sponsorable_login', 'amount')
    sponsorable_id = sgqlc.types.Field(ID, graphql_name='sponsorableId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')


class CancelEnterpriseAdminInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='invitationId')


class CancelEnterpriseMemberInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='invitationId')


class CancelSponsorshipInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsor_id', 'sponsor_login', 'sponsorable_id', 'sponsorable_login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsor_id = sgqlc.types.Field(ID, graphql_name='sponsorId')
    sponsor_login = sgqlc.types.Field(String, graphql_name='sponsorLogin')
    sponsorable_id = sgqlc.types.Field(ID, graphql_name='sponsorableId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')


class ChangeUserStatusInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'emoji', 'message', 'organization_id', 'limited_availability', 'expires_at')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    emoji = sgqlc.types.Field(String, graphql_name='emoji')
    message = sgqlc.types.Field(String, graphql_name='message')
    organization_id = sgqlc.types.Field(ID, graphql_name='organizationId')
    limited_availability = sgqlc.types.Field(Boolean, graphql_name='limitedAvailability')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')


class CheckAnnotationData(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('path', 'location', 'annotation_level', 'message', 'title', 'raw_details')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    location = sgqlc.types.Field(sgqlc.types.non_null('CheckAnnotationRange'), graphql_name='location')
    annotation_level = sgqlc.types.Field(sgqlc.types.non_null(CheckAnnotationLevel), graphql_name='annotationLevel')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    title = sgqlc.types.Field(String, graphql_name='title')
    raw_details = sgqlc.types.Field(String, graphql_name='rawDetails')


class CheckAnnotationRange(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('start_line', 'start_column', 'end_line', 'end_column')
    start_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startLine')
    start_column = sgqlc.types.Field(Int, graphql_name='startColumn')
    end_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endLine')
    end_column = sgqlc.types.Field(Int, graphql_name='endColumn')


class CheckRunAction(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('label', 'description', 'identifier')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')


class CheckRunFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('check_type', 'app_id', 'check_name', 'status', 'statuses', 'conclusions')
    check_type = sgqlc.types.Field(CheckRunType, graphql_name='checkType')
    app_id = sgqlc.types.Field(Int, graphql_name='appId')
    check_name = sgqlc.types.Field(String, graphql_name='checkName')
    status = sgqlc.types.Field(CheckStatusState, graphql_name='status')
    statuses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CheckStatusState)), graphql_name='statuses')
    conclusions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CheckConclusionState)), graphql_name='conclusions')


class CheckRunOutput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('title', 'summary', 'text', 'annotations', 'images')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    text = sgqlc.types.Field(String, graphql_name='text')
    annotations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CheckAnnotationData)), graphql_name='annotations')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CheckRunOutputImage')), graphql_name='images')


class CheckRunOutputImage(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alt', 'image_url', 'caption')
    alt = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alt')
    image_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='imageUrl')
    caption = sgqlc.types.Field(String, graphql_name='caption')


class CheckSuiteAutoTriggerPreference(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('app_id', 'setting')
    app_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='appId')
    setting = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setting')


class CheckSuiteFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('app_id', 'check_name')
    app_id = sgqlc.types.Field(Int, graphql_name='appId')
    check_name = sgqlc.types.Field(String, graphql_name='checkName')


class ClearLabelsFromLabelableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'labelable_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='labelableId')


class ClearProjectV2ItemFieldValueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'item_id', 'field_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')
    field_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fieldId')


class CloneProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'target_owner_id', 'source_id', 'include_workflows', 'name', 'body', 'public')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    target_owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='targetOwnerId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sourceId')
    include_workflows = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeWorkflows')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    public = sgqlc.types.Field(Boolean, graphql_name='public')


class CloneTemplateRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name', 'owner_id', 'description', 'visibility', 'include_all_branches')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    description = sgqlc.types.Field(String, graphql_name='description')
    visibility = sgqlc.types.Field(sgqlc.types.non_null(RepositoryVisibility), graphql_name='visibility')
    include_all_branches = sgqlc.types.Field(Boolean, graphql_name='includeAllBranches')


class CloseDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion_id', 'reason')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='discussionId')
    reason = sgqlc.types.Field(DiscussionCloseReason, graphql_name='reason')


class CloseIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'state_reason', 'duplicate_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    state_reason = sgqlc.types.Field(IssueClosedStateReason, graphql_name='stateReason')
    duplicate_issue_id = sgqlc.types.Field(ID, graphql_name='duplicateIssueId')


class ClosePullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class CodeScanningParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('code_scanning_tools',)
    code_scanning_tools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CodeScanningToolInput'))), graphql_name='codeScanningTools')


class CodeScanningToolInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alerts_threshold', 'security_alerts_threshold', 'tool')
    alerts_threshold = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alertsThreshold')
    security_alerts_threshold = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='securityAlertsThreshold')
    tool = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tool')


class CommitAuthor(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'emails')
    id = sgqlc.types.Field(ID, graphql_name='id')
    emails = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='emails')


class CommitAuthorEmailPatternParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(Boolean, graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class CommitContributionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(CommitContributionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class CommitMessage(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('headline', 'body')
    headline = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headline')
    body = sgqlc.types.Field(String, graphql_name='body')


class CommitMessagePatternParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(Boolean, graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class CommittableBranch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'repository_name_with_owner', 'branch_name')
    id = sgqlc.types.Field(ID, graphql_name='id')
    repository_name_with_owner = sgqlc.types.Field(String, graphql_name='repositoryNameWithOwner')
    branch_name = sgqlc.types.Field(String, graphql_name='branchName')


class CommitterEmailPatternParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(Boolean, graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class ContributionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('direction',)
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ConvertProjectCardNoteToIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_card_id', 'repository_id', 'title', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectCardId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')


class ConvertProjectV2DraftIssueItemToIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class ConvertPullRequestToDraftInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class CopilotCodeReviewParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('review_draft_pull_requests', 'review_on_push')
    review_draft_pull_requests = sgqlc.types.Field(Boolean, graphql_name='reviewDraftPullRequests')
    review_on_push = sgqlc.types.Field(Boolean, graphql_name='reviewOnPush')


class CopyProjectV2Input(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'owner_id', 'title', 'include_draft_issues')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    include_draft_issues = sgqlc.types.Field(Boolean, graphql_name='includeDraftIssues')


class CreateAttributionInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'source_id', 'target_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sourceId')
    target_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='targetId')


class CreateBranchProtectionRuleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'pattern', 'requires_approving_reviews', 'required_approving_review_count', 'requires_commit_signatures', 'requires_linear_history', 'blocks_creations', 'allows_force_pushes', 'allows_deletions', 'is_admin_enforced', 'requires_status_checks', 'requires_strict_status_checks', 'requires_code_owner_reviews', 'dismisses_stale_reviews', 'restricts_review_dismissals', 'review_dismissal_actor_ids', 'bypass_pull_request_actor_ids', 'bypass_force_push_actor_ids', 'restricts_pushes', 'push_actor_ids', 'required_status_check_contexts', 'required_status_checks', 'requires_deployments', 'required_deployment_environments', 'requires_conversation_resolution', 'require_last_push_approval', 'lock_branch', 'lock_allows_fetch_and_merge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')
    requires_approving_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresApprovingReviews')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    requires_commit_signatures = sgqlc.types.Field(Boolean, graphql_name='requiresCommitSignatures')
    requires_linear_history = sgqlc.types.Field(Boolean, graphql_name='requiresLinearHistory')
    blocks_creations = sgqlc.types.Field(Boolean, graphql_name='blocksCreations')
    allows_force_pushes = sgqlc.types.Field(Boolean, graphql_name='allowsForcePushes')
    allows_deletions = sgqlc.types.Field(Boolean, graphql_name='allowsDeletions')
    is_admin_enforced = sgqlc.types.Field(Boolean, graphql_name='isAdminEnforced')
    requires_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStatusChecks')
    requires_strict_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStrictStatusChecks')
    requires_code_owner_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresCodeOwnerReviews')
    dismisses_stale_reviews = sgqlc.types.Field(Boolean, graphql_name='dismissesStaleReviews')
    restricts_review_dismissals = sgqlc.types.Field(Boolean, graphql_name='restrictsReviewDismissals')
    review_dismissal_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='reviewDismissalActorIds')
    bypass_pull_request_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='bypassPullRequestActorIds')
    bypass_force_push_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='bypassForcePushActorIds')
    restricts_pushes = sgqlc.types.Field(Boolean, graphql_name='restrictsPushes')
    push_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='pushActorIds')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredStatusCheckContexts')
    required_status_checks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RequiredStatusCheckInput')), graphql_name='requiredStatusChecks')
    requires_deployments = sgqlc.types.Field(Boolean, graphql_name='requiresDeployments')
    required_deployment_environments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredDeploymentEnvironments')
    requires_conversation_resolution = sgqlc.types.Field(Boolean, graphql_name='requiresConversationResolution')
    require_last_push_approval = sgqlc.types.Field(Boolean, graphql_name='requireLastPushApproval')
    lock_branch = sgqlc.types.Field(Boolean, graphql_name='lockBranch')
    lock_allows_fetch_and_merge = sgqlc.types.Field(Boolean, graphql_name='lockAllowsFetchAndMerge')


class CreateCheckRunInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name', 'head_sha', 'details_url', 'external_id', 'status', 'started_at', 'conclusion', 'completed_at', 'output', 'actions')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    head_sha = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='headSha')
    details_url = sgqlc.types.Field(URI, graphql_name='detailsUrl')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    status = sgqlc.types.Field(RequestableCheckStatusState, graphql_name='status')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    conclusion = sgqlc.types.Field(CheckConclusionState, graphql_name='conclusion')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    output = sgqlc.types.Field(CheckRunOutput, graphql_name='output')
    actions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CheckRunAction)), graphql_name='actions')


class CreateCheckSuiteInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'head_sha')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    head_sha = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='headSha')


class CreateCommitOnBranchInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'branch', 'file_changes', 'message', 'expected_head_oid')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    branch = sgqlc.types.Field(sgqlc.types.non_null(CommittableBranch), graphql_name='branch')
    file_changes = sgqlc.types.Field('FileChanges', graphql_name='fileChanges')
    message = sgqlc.types.Field(sgqlc.types.non_null(CommitMessage), graphql_name='message')
    expected_head_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='expectedHeadOid')


class CreateDeploymentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'ref_id', 'auto_merge', 'required_contexts', 'description', 'environment', 'task', 'payload')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    ref_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='refId')
    auto_merge = sgqlc.types.Field(Boolean, graphql_name='autoMerge')
    required_contexts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredContexts')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    task = sgqlc.types.Field(String, graphql_name='task')
    payload = sgqlc.types.Field(String, graphql_name='payload')


class CreateDeploymentStatusInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deployment_id', 'state', 'description', 'environment', 'environment_url', 'auto_inactive', 'log_url')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deployment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='deploymentId')
    state = sgqlc.types.Field(sgqlc.types.non_null(DeploymentStatusState), graphql_name='state')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    environment_url = sgqlc.types.Field(String, graphql_name='environmentUrl')
    auto_inactive = sgqlc.types.Field(Boolean, graphql_name='autoInactive')
    log_url = sgqlc.types.Field(String, graphql_name='logUrl')


class CreateDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'title', 'body', 'category_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    category_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='categoryId')


class CreateEnterpriseOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login', 'profile_name', 'billing_email', 'admin_logins')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    profile_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='profileName')
    billing_email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billingEmail')
    admin_logins = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='adminLogins')


class CreateEnvironmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateIpAllowListEntryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'allow_list_value', 'name', 'is_active')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    allow_list_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='allowListValue')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')


class CreateIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'title', 'body', 'assignee_ids', 'milestone_id', 'label_ids', 'project_ids', 'issue_template', 'issue_type_id', 'parent_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')
    milestone_id = sgqlc.types.Field(ID, graphql_name='milestoneId')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    project_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectIds')
    issue_template = sgqlc.types.Field(String, graphql_name='issueTemplate')
    issue_type_id = sgqlc.types.Field(ID, graphql_name='issueTypeId')
    parent_issue_id = sgqlc.types.Field(ID, graphql_name='parentIssueId')


class CreateIssueTypeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'is_enabled', 'name', 'description', 'color')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    is_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEnabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    color = sgqlc.types.Field(IssueTypeColor, graphql_name='color')


class CreateLabelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'color', 'name', 'description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class CreateLinkedBranchInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'oid', 'name', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    name = sgqlc.types.Field(String, graphql_name='name')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')


class CreateMigrationSourceInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'name', 'url', 'access_token', 'type', 'owner_id', 'github_pat')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')
    access_token = sgqlc.types.Field(String, graphql_name='accessToken')
    type = sgqlc.types.Field(sgqlc.types.non_null(MigrationSourceType), graphql_name='type')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    github_pat = sgqlc.types.Field(String, graphql_name='githubPat')


class CreateProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'name', 'body', 'template', 'repository_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    template = sgqlc.types.Field(ProjectTemplate, graphql_name='template')
    repository_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds')


class CreateProjectV2FieldInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'data_type', 'name', 'single_select_options', 'iteration_configuration')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    data_type = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2CustomFieldType), graphql_name='dataType')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    single_select_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProjectV2SingleSelectFieldOptionInput')), graphql_name='singleSelectOptions')
    iteration_configuration = sgqlc.types.Field('ProjectV2IterationFieldConfigurationInput', graphql_name='iterationConfiguration')


class CreateProjectV2Input(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'title', 'repository_id', 'team_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')


class CreateProjectV2StatusUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'start_date', 'target_date', 'status', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    start_date = sgqlc.types.Field(Date, graphql_name='startDate')
    target_date = sgqlc.types.Field(Date, graphql_name='targetDate')
    status = sgqlc.types.Field(ProjectV2StatusUpdateStatus, graphql_name='status')
    body = sgqlc.types.Field(String, graphql_name='body')


class CreatePullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'base_ref_name', 'head_ref_name', 'head_repository_id', 'title', 'body', 'maintainer_can_modify', 'draft')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    base_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='baseRefName')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    head_repository_id = sgqlc.types.Field(ID, graphql_name='headRepositoryId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    maintainer_can_modify = sgqlc.types.Field(Boolean, graphql_name='maintainerCanModify')
    draft = sgqlc.types.Field(Boolean, graphql_name='draft')


class CreateRefInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name', 'oid')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')


class CreateRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'name', 'owner_id', 'description', 'visibility', 'template', 'homepage_url', 'has_wiki_enabled', 'has_issues_enabled', 'team_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner_id = sgqlc.types.Field(ID, graphql_name='ownerId')
    description = sgqlc.types.Field(String, graphql_name='description')
    visibility = sgqlc.types.Field(sgqlc.types.non_null(RepositoryVisibility), graphql_name='visibility')
    template = sgqlc.types.Field(Boolean, graphql_name='template')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    has_wiki_enabled = sgqlc.types.Field(Boolean, graphql_name='hasWikiEnabled')
    has_issues_enabled = sgqlc.types.Field(Boolean, graphql_name='hasIssuesEnabled')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')


class CreateRepositoryRulesetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'source_id', 'name', 'target', 'rules', 'conditions', 'enforcement', 'bypass_actors')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sourceId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(RepositoryRulesetTarget, graphql_name='target')
    rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryRuleInput')), graphql_name='rules')
    conditions = sgqlc.types.Field(sgqlc.types.non_null('RepositoryRuleConditionsInput'), graphql_name='conditions')
    enforcement = sgqlc.types.Field(sgqlc.types.non_null(RuleEnforcement), graphql_name='enforcement')
    bypass_actors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryRulesetBypassActorInput')), graphql_name='bypassActors')


class CreateSponsorsListingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsorable_login', 'fiscal_host_login', 'fiscally_hosted_project_profile_url', 'billing_country_or_region_code', 'residence_country_or_region_code', 'contact_email', 'full_description')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')
    fiscal_host_login = sgqlc.types.Field(String, graphql_name='fiscalHostLogin')
    fiscally_hosted_project_profile_url = sgqlc.types.Field(String, graphql_name='fiscallyHostedProjectProfileUrl')
    billing_country_or_region_code = sgqlc.types.Field(SponsorsCountryOrRegionCode, graphql_name='billingCountryOrRegionCode')
    residence_country_or_region_code = sgqlc.types.Field(SponsorsCountryOrRegionCode, graphql_name='residenceCountryOrRegionCode')
    contact_email = sgqlc.types.Field(String, graphql_name='contactEmail')
    full_description = sgqlc.types.Field(String, graphql_name='fullDescription')


class CreateSponsorsTierInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsorable_id', 'sponsorable_login', 'amount', 'is_recurring', 'repository_id', 'repository_owner_login', 'repository_name', 'welcome_message', 'description', 'publish')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsorable_id = sgqlc.types.Field(ID, graphql_name='sponsorableId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')
    is_recurring = sgqlc.types.Field(Boolean, graphql_name='isRecurring')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    repository_owner_login = sgqlc.types.Field(String, graphql_name='repositoryOwnerLogin')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    welcome_message = sgqlc.types.Field(String, graphql_name='welcomeMessage')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    publish = sgqlc.types.Field(Boolean, graphql_name='publish')


class CreateSponsorshipInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsor_id', 'sponsor_login', 'sponsorable_id', 'sponsorable_login', 'tier_id', 'amount', 'is_recurring', 'receive_emails', 'privacy_level')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsor_id = sgqlc.types.Field(ID, graphql_name='sponsorId')
    sponsor_login = sgqlc.types.Field(String, graphql_name='sponsorLogin')
    sponsorable_id = sgqlc.types.Field(ID, graphql_name='sponsorableId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')
    tier_id = sgqlc.types.Field(ID, graphql_name='tierId')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    is_recurring = sgqlc.types.Field(Boolean, graphql_name='isRecurring')
    receive_emails = sgqlc.types.Field(Boolean, graphql_name='receiveEmails')
    privacy_level = sgqlc.types.Field(SponsorshipPrivacy, graphql_name='privacyLevel')


class CreateSponsorshipsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsor_login', 'sponsorships', 'receive_emails', 'privacy_level', 'recurring')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsor_login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sponsorLogin')
    sponsorships = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BulkSponsorship))), graphql_name='sponsorships')
    receive_emails = sgqlc.types.Field(Boolean, graphql_name='receiveEmails')
    privacy_level = sgqlc.types.Field(SponsorshipPrivacy, graphql_name='privacyLevel')
    recurring = sgqlc.types.Field(Boolean, graphql_name='recurring')


class CreateTeamDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_id = sgqlc.types.Field(ID, graphql_name='discussionId')
    body = sgqlc.types.Field(String, graphql_name='body')


class CreateTeamDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'team_id', 'title', 'body', 'private')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    private = sgqlc.types.Field(Boolean, graphql_name='private')


class CreateUserListInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'name', 'description', 'is_private')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_private = sgqlc.types.Field(Boolean, graphql_name='isPrivate')


class DeclineTopicSuggestionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name', 'reason')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(ID, graphql_name='repositoryId')
    name = sgqlc.types.Field(String, graphql_name='name')
    reason = sgqlc.types.Field(TopicSuggestionDeclineReason, graphql_name='reason')


class DeleteBranchProtectionRuleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'branch_protection_rule_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    branch_protection_rule_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='branchProtectionRuleId')


class DeleteDeploymentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteEnvironmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteIpAllowListEntryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ip_allow_list_entry_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ip_allow_list_entry_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ipAllowListEntryId')


class DeleteIssueCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class DeleteIssueTypeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_type_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueTypeId')


class DeleteLabelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteLinkedBranchInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'linked_branch_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    linked_branch_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkedBranchId')


class DeletePackageVersionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'package_version_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    package_version_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='packageVersionId')


class DeleteProjectCardInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'card_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cardId')


class DeleteProjectColumnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'column_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')


class DeleteProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class DeleteProjectV2FieldInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'field_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    field_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fieldId')


class DeleteProjectV2Input(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class DeleteProjectV2ItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'item_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')


class DeleteProjectV2StatusUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'status_update_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    status_update_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='statusUpdateId')


class DeleteProjectV2WorkflowInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'workflow_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workflow_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workflowId')


class DeletePullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeletePullRequestReviewInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')


class DeleteRefInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ref_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ref_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='refId')


class DeleteRepositoryRulesetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_ruleset_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_ruleset_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryRulesetId')


class DeleteTeamDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteTeamDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteUserListInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'list_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    list_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='listId')


class DeleteVerifiableDomainInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeploymentOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(DeploymentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class DequeuePullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DisablePullRequestAutoMergeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class DiscussionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(DiscussionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class DiscussionPollOptionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(DiscussionPollOptionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class DismissPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review_id', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')


class DismissRepositoryVulnerabilityAlertInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_vulnerability_alert_id', 'dismiss_reason')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_vulnerability_alert_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryVulnerabilityAlertId')
    dismiss_reason = sgqlc.types.Field(sgqlc.types.non_null(DismissReason), graphql_name='dismissReason')


class DraftPullRequestReviewComment(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('path', 'position', 'body')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class DraftPullRequestReviewThread(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('path', 'line', 'side', 'start_line', 'start_side', 'body')
    path = sgqlc.types.Field(String, graphql_name='path')
    line = sgqlc.types.Field(Int, graphql_name='line')
    side = sgqlc.types.Field(DiffSide, graphql_name='side')
    start_line = sgqlc.types.Field(Int, graphql_name='startLine')
    start_side = sgqlc.types.Field(DiffSide, graphql_name='startSide')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class EnablePullRequestAutoMergeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'commit_headline', 'commit_body', 'merge_method', 'author_email', 'expected_head_oid')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    commit_headline = sgqlc.types.Field(String, graphql_name='commitHeadline')
    commit_body = sgqlc.types.Field(String, graphql_name='commitBody')
    merge_method = sgqlc.types.Field(PullRequestMergeMethod, graphql_name='mergeMethod')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    expected_head_oid = sgqlc.types.Field(GitObjectID, graphql_name='expectedHeadOid')


class EnqueuePullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'jump', 'expected_head_oid')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    jump = sgqlc.types.Field(Boolean, graphql_name='jump')
    expected_head_oid = sgqlc.types.Field(GitObjectID, graphql_name='expectedHeadOid')


class EnterpriseAdministratorInvitationOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorInvitationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseMemberInvitationOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberInvitationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseMemberOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerInstallationOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerUserAccountEmailOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountEmailOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerUserAccountOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerUserAccountsUploadOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountsUploadOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class Environments(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(EnvironmentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class FileAddition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('path', 'contents')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    contents = sgqlc.types.Field(sgqlc.types.non_null(Base64String), graphql_name='contents')


class FileChanges(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('deletions', 'additions')
    deletions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FileDeletion')), graphql_name='deletions')
    additions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FileAddition)), graphql_name='additions')


class FileDeletion(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('path',)
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')


class FileExtensionRestrictionParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('restricted_file_extensions',)
    restricted_file_extensions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='restrictedFileExtensions')


class FilePathRestrictionParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('restricted_file_paths',)
    restricted_file_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='restrictedFilePaths')


class FollowOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')


class FollowUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')


class GistOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(GistOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class GrantEnterpriseOrganizationsMigratorRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')


class GrantMigratorRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id', 'actor', 'actor_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    actor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='actor')
    actor_type = sgqlc.types.Field(sgqlc.types.non_null(ActorType), graphql_name='actorType')


class ImportProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_name', 'name', 'body', 'public', 'column_imports')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ownerName')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    public = sgqlc.types.Field(Boolean, graphql_name='public')
    column_imports = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectColumnImport'))), graphql_name='columnImports')


class InviteEnterpriseAdminInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'invitee', 'email', 'role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    invitee = sgqlc.types.Field(String, graphql_name='invitee')
    email = sgqlc.types.Field(String, graphql_name='email')
    role = sgqlc.types.Field(EnterpriseAdministratorRole, graphql_name='role')


class InviteEnterpriseMemberInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'invitee', 'email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    invitee = sgqlc.types.Field(String, graphql_name='invitee')
    email = sgqlc.types.Field(String, graphql_name='email')


class IpAllowListEntryOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListEntryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class IssueCommentOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class IssueDependencyOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueDependencyOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class IssueFilters(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('assignee', 'created_by', 'labels', 'mentioned', 'milestone', 'milestone_number', 'since', 'states', 'type', 'viewer_subscribed')
    assignee = sgqlc.types.Field(String, graphql_name='assignee')
    created_by = sgqlc.types.Field(String, graphql_name='createdBy')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')
    mentioned = sgqlc.types.Field(String, graphql_name='mentioned')
    milestone = sgqlc.types.Field(String, graphql_name='milestone')
    milestone_number = sgqlc.types.Field(String, graphql_name='milestoneNumber')
    since = sgqlc.types.Field(DateTime, graphql_name='since')
    states = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states')
    type = sgqlc.types.Field(String, graphql_name='type')
    viewer_subscribed = sgqlc.types.Field(Boolean, graphql_name='viewerSubscribed')


class IssueOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class IssueTypeOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueTypeOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class LabelOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(LabelOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class LanguageOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(LanguageOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class LinkProjectV2ToRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class LinkProjectV2ToTeamInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'team_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='teamId')


class LinkRepositoryToProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class LockLockableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'lockable_id', 'lock_reason')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    lockable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='lockableId')
    lock_reason = sgqlc.types.Field(LockReason, graphql_name='lockReason')


class MannequinOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(MannequinOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class MarkDiscussionCommentAsAnswerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MarkFileAsViewedInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'path')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')


class MarkProjectV2AsTemplateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class MarkPullRequestReadyForReviewInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class MaxFilePathLengthParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('max_file_path_length',)
    max_file_path_length = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxFilePathLength')


class MaxFileSizeParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('max_file_size',)
    max_file_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxFileSize')


class MergeBranchInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'base', 'head', 'commit_message', 'author_email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    base = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='base')
    head = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='head')
    commit_message = sgqlc.types.Field(String, graphql_name='commitMessage')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')


class MergePullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'commit_headline', 'commit_body', 'expected_head_oid', 'merge_method', 'author_email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    commit_headline = sgqlc.types.Field(String, graphql_name='commitHeadline')
    commit_body = sgqlc.types.Field(String, graphql_name='commitBody')
    expected_head_oid = sgqlc.types.Field(GitObjectID, graphql_name='expectedHeadOid')
    merge_method = sgqlc.types.Field(PullRequestMergeMethod, graphql_name='mergeMethod')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')


class MergeQueueParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('check_response_timeout_minutes', 'grouping_strategy', 'max_entries_to_build', 'max_entries_to_merge', 'merge_method', 'min_entries_to_merge', 'min_entries_to_merge_wait_minutes')
    check_response_timeout_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='checkResponseTimeoutMinutes')
    grouping_strategy = sgqlc.types.Field(sgqlc.types.non_null(MergeQueueGroupingStrategy), graphql_name='groupingStrategy')
    max_entries_to_build = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxEntriesToBuild')
    max_entries_to_merge = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxEntriesToMerge')
    merge_method = sgqlc.types.Field(sgqlc.types.non_null(MergeQueueMergeMethod), graphql_name='mergeMethod')
    min_entries_to_merge = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minEntriesToMerge')
    min_entries_to_merge_wait_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minEntriesToMergeWaitMinutes')


class MilestoneOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(MilestoneOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class MinimizeCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id', 'classifier')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    classifier = sgqlc.types.Field(sgqlc.types.non_null(ReportedContentClassifiers), graphql_name='classifier')


class MoveProjectCardInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'card_id', 'column_id', 'after_card_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cardId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    after_card_id = sgqlc.types.Field(ID, graphql_name='afterCardId')


class MoveProjectColumnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'column_id', 'after_column_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    after_column_id = sgqlc.types.Field(ID, graphql_name='afterColumnId')


class OrgEnterpriseOwnerOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(OrgEnterpriseOwnerOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class OrganizationOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(OrganizationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class OrganizationPropertyConditionTargetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('exclude', 'include')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationPropertyTargetDefinitionInput'))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationPropertyTargetDefinitionInput'))), graphql_name='include')


class OrganizationPropertyTargetDefinitionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'property_values')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='propertyValues')


class PackageFileOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(PackageFileOrderField, graphql_name='field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')


class PackageOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(PackageOrderField, graphql_name='field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')


class PackageVersionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(PackageVersionOrderField, graphql_name='field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')


class PinEnvironmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment_id', 'pinned')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='environmentId')
    pinned = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pinned')


class PinIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class PinnedEnvironmentOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(PinnedEnvironmentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectCardImport(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('repository', 'number')
    repository = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repository')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class ProjectColumnImport(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('column_name', 'position', 'issues')
    column_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='columnName')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    issues = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProjectCardImport)), graphql_name='issues')


class ProjectOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2Collaborator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('user_id', 'team_id', 'role')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    role = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2Roles), graphql_name='role')


class ProjectV2FieldOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2FieldOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2FieldValue(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('text', 'number', 'date', 'single_select_option_id', 'iteration_id')
    text = sgqlc.types.Field(String, graphql_name='text')
    number = sgqlc.types.Field(Float, graphql_name='number')
    date = sgqlc.types.Field(Date, graphql_name='date')
    single_select_option_id = sgqlc.types.Field(String, graphql_name='singleSelectOptionId')
    iteration_id = sgqlc.types.Field(String, graphql_name='iterationId')


class ProjectV2Filters(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('state',)
    state = sgqlc.types.Field(ProjectV2State, graphql_name='state')


class ProjectV2ItemFieldValueOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemFieldValueOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2ItemOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2Iteration(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('start_date', 'duration', 'title')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='startDate')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ProjectV2IterationFieldConfigurationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('start_date', 'duration', 'iterations')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='startDate')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    iterations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectV2Iteration))), graphql_name='iterations')


class ProjectV2Order(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2OrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2SingleSelectFieldOptionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'color', 'description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    color = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2SingleSelectFieldOptionColor), graphql_name='color')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class ProjectV2StatusOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2StatusUpdateOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2ViewOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ViewOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectV2WorkflowOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2WorkflowsOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class PropertyTargetDefinitionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'property_values', 'source')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='propertyValues')
    source = sgqlc.types.Field(String, graphql_name='source')


class PublishSponsorsTierInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tier_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tier_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='tierId')


class PullRequestOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(PullRequestOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class PullRequestParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('allowed_merge_methods', 'automatic_copilot_code_review_enabled', 'dismiss_stale_reviews_on_push', 'require_code_owner_review', 'require_last_push_approval', 'required_approving_review_count', 'required_review_thread_resolution')
    allowed_merge_methods = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestAllowedMergeMethods)), graphql_name='allowedMergeMethods')
    automatic_copilot_code_review_enabled = sgqlc.types.Field(Boolean, graphql_name='automaticCopilotCodeReviewEnabled')
    dismiss_stale_reviews_on_push = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dismissStaleReviewsOnPush')
    require_code_owner_review = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requireCodeOwnerReview')
    require_last_push_approval = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requireLastPushApproval')
    required_approving_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='requiredApprovingReviewCount')
    required_review_thread_resolution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiredReviewThreadResolution')


class ReactionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ReactionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RefNameConditionTargetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('exclude', 'include')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='include')


class RefOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(RefOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RefUpdate(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'after_oid', 'before_oid', 'force')
    name = sgqlc.types.Field(sgqlc.types.non_null(GitRefname), graphql_name='name')
    after_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='afterOid')
    before_oid = sgqlc.types.Field(GitObjectID, graphql_name='beforeOid')
    force = sgqlc.types.Field(Boolean, graphql_name='force')


class RegenerateEnterpriseIdentityProviderRecoveryCodesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')


class RegenerateVerifiableDomainTokenInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RejectDeploymentsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'workflow_run_id', 'environment_ids', 'comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    workflow_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workflowRunId')
    environment_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='environmentIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class ReleaseOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(ReleaseOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RemoveAssigneesFromAssignableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'assignable_id', 'assignee_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    assignable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='assignableId')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')


class RemoveBlockedByInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'blocking_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    blocking_issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='blockingIssueId')


class RemoveEnterpriseAdminInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')


class RemoveEnterpriseIdentityProviderInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')


class RemoveEnterpriseMemberInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')


class RemoveEnterpriseOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'organization_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')


class RemoveEnterpriseSupportEntitlementInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')


class RemoveLabelsFromLabelableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'labelable_id', 'label_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='labelableId')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='labelIds')


class RemoveOutsideCollaboratorInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id', 'organization_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')


class RemoveReactionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id', 'content')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')


class RemoveStarInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'starrable_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='starrableId')


class RemoveSubIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'sub_issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    sub_issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subIssueId')


class RemoveUpvoteInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')


class ReopenDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='discussionId')


class ReopenIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class ReopenPullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')


class ReorderEnvironmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment_id', 'position')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='environmentId')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')


class ReplaceActorsForAssignableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'assignable_id', 'actor_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    assignable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='assignableId')
    actor_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='actorIds')


class RepositoryIdConditionTargetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('repository_ids',)
    repository_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='repositoryIds')


class RepositoryInvitationOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInvitationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RepositoryMigrationOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryMigrationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(RepositoryMigrationOrderDirection), graphql_name='direction')


class RepositoryNameConditionTargetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('exclude', 'include', 'protected')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='include')
    protected = sgqlc.types.Field(Boolean, graphql_name='protected')


class RepositoryOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RepositoryPropertyConditionTargetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('exclude', 'include')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PropertyTargetDefinitionInput))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PropertyTargetDefinitionInput))), graphql_name='include')


class RepositoryRuleConditionsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ref_name', 'repository_name', 'repository_id', 'repository_property', 'organization_property')
    ref_name = sgqlc.types.Field(RefNameConditionTargetInput, graphql_name='refName')
    repository_name = sgqlc.types.Field(RepositoryNameConditionTargetInput, graphql_name='repositoryName')
    repository_id = sgqlc.types.Field(RepositoryIdConditionTargetInput, graphql_name='repositoryId')
    repository_property = sgqlc.types.Field(RepositoryPropertyConditionTargetInput, graphql_name='repositoryProperty')
    organization_property = sgqlc.types.Field(OrganizationPropertyConditionTargetInput, graphql_name='organizationProperty')


class RepositoryRuleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'type', 'parameters')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(RepositoryRuleType), graphql_name='type')
    parameters = sgqlc.types.Field('RuleParametersInput', graphql_name='parameters')


class RepositoryRuleOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryRuleOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RepositoryRulesetBypassActorInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('actor_id', 'repository_role_database_id', 'organization_admin', 'enterprise_owner', 'deploy_key', 'bypass_mode')
    actor_id = sgqlc.types.Field(ID, graphql_name='actorId')
    repository_role_database_id = sgqlc.types.Field(Int, graphql_name='repositoryRoleDatabaseId')
    organization_admin = sgqlc.types.Field(Boolean, graphql_name='organizationAdmin')
    enterprise_owner = sgqlc.types.Field(Boolean, graphql_name='enterpriseOwner')
    deploy_key = sgqlc.types.Field(Boolean, graphql_name='deployKey')
    bypass_mode = sgqlc.types.Field(sgqlc.types.non_null(RepositoryRulesetBypassActorBypassMode), graphql_name='bypassMode')


class ReprioritizeSubIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'sub_issue_id', 'after_id', 'before_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    sub_issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subIssueId')
    after_id = sgqlc.types.Field(ID, graphql_name='afterId')
    before_id = sgqlc.types.Field(ID, graphql_name='beforeId')


class RequestReviewsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'user_ids', 'bot_ids', 'team_ids', 'union')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='userIds')
    bot_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='botIds')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='teamIds')
    union = sgqlc.types.Field(Boolean, graphql_name='union')


class RequiredDeploymentsParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('required_deployment_environments',)
    required_deployment_environments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='requiredDeploymentEnvironments')


class RequiredStatusCheckInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('context', 'app_id')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')
    app_id = sgqlc.types.Field(ID, graphql_name='appId')


class RequiredStatusChecksParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('do_not_enforce_on_create', 'required_status_checks', 'strict_required_status_checks_policy')
    do_not_enforce_on_create = sgqlc.types.Field(Boolean, graphql_name='doNotEnforceOnCreate')
    required_status_checks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatusCheckConfigurationInput'))), graphql_name='requiredStatusChecks')
    strict_required_status_checks_policy = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='strictRequiredStatusChecksPolicy')


class RerequestCheckSuiteInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'check_suite_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    check_suite_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='checkSuiteId')


class ResolveReviewThreadInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'thread_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='threadId')


class RetireSponsorsTierInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tier_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tier_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='tierId')


class RevertPullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'title', 'body', 'draft')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    draft = sgqlc.types.Field(Boolean, graphql_name='draft')


class RevokeEnterpriseOrganizationsMigratorRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')


class RevokeMigratorRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id', 'actor', 'actor_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    actor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='actor')
    actor_type = sgqlc.types.Field(sgqlc.types.non_null(ActorType), graphql_name='actorType')


class RuleParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('update', 'merge_queue', 'required_deployments', 'pull_request', 'required_status_checks', 'commit_message_pattern', 'commit_author_email_pattern', 'committer_email_pattern', 'branch_name_pattern', 'tag_name_pattern', 'file_path_restriction', 'max_file_path_length', 'file_extension_restriction', 'max_file_size', 'workflows', 'code_scanning', 'copilot_code_review')
    update = sgqlc.types.Field('UpdateParametersInput', graphql_name='update')
    merge_queue = sgqlc.types.Field(MergeQueueParametersInput, graphql_name='mergeQueue')
    required_deployments = sgqlc.types.Field(RequiredDeploymentsParametersInput, graphql_name='requiredDeployments')
    pull_request = sgqlc.types.Field(PullRequestParametersInput, graphql_name='pullRequest')
    required_status_checks = sgqlc.types.Field(RequiredStatusChecksParametersInput, graphql_name='requiredStatusChecks')
    commit_message_pattern = sgqlc.types.Field(CommitMessagePatternParametersInput, graphql_name='commitMessagePattern')
    commit_author_email_pattern = sgqlc.types.Field(CommitAuthorEmailPatternParametersInput, graphql_name='commitAuthorEmailPattern')
    committer_email_pattern = sgqlc.types.Field(CommitterEmailPatternParametersInput, graphql_name='committerEmailPattern')
    branch_name_pattern = sgqlc.types.Field(BranchNamePatternParametersInput, graphql_name='branchNamePattern')
    tag_name_pattern = sgqlc.types.Field('TagNamePatternParametersInput', graphql_name='tagNamePattern')
    file_path_restriction = sgqlc.types.Field(FilePathRestrictionParametersInput, graphql_name='filePathRestriction')
    max_file_path_length = sgqlc.types.Field(MaxFilePathLengthParametersInput, graphql_name='maxFilePathLength')
    file_extension_restriction = sgqlc.types.Field(FileExtensionRestrictionParametersInput, graphql_name='fileExtensionRestriction')
    max_file_size = sgqlc.types.Field(MaxFileSizeParametersInput, graphql_name='maxFileSize')
    workflows = sgqlc.types.Field('WorkflowsParametersInput', graphql_name='workflows')
    code_scanning = sgqlc.types.Field(CodeScanningParametersInput, graphql_name='codeScanning')
    copilot_code_review = sgqlc.types.Field(CopilotCodeReviewParametersInput, graphql_name='copilotCodeReview')


class SavedReplyOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SavedReplyOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SecurityAdvisoryIdentifierFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('type', 'value')
    type = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryIdentifierType), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class SecurityAdvisoryOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SecurityVulnerabilityOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SecurityVulnerabilityOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SetEnterpriseIdentityProviderInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'sso_url', 'issuer', 'idp_certificate', 'signature_method', 'digest_method')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    sso_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='ssoUrl')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    idp_certificate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='idpCertificate')
    signature_method = sgqlc.types.Field(sgqlc.types.non_null(SamlSignatureAlgorithm), graphql_name='signatureMethod')
    digest_method = sgqlc.types.Field(sgqlc.types.non_null(SamlDigestAlgorithm), graphql_name='digestMethod')


class SetOrganizationInteractionLimitInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id', 'limit', 'expiry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    limit = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInteractionLimit), graphql_name='limit')
    expiry = sgqlc.types.Field(RepositoryInteractionLimitExpiry, graphql_name='expiry')


class SetRepositoryInteractionLimitInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'limit', 'expiry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    limit = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInteractionLimit), graphql_name='limit')
    expiry = sgqlc.types.Field(RepositoryInteractionLimitExpiry, graphql_name='expiry')


class SetUserInteractionLimitInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id', 'limit', 'expiry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    limit = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInteractionLimit), graphql_name='limit')
    expiry = sgqlc.types.Field(RepositoryInteractionLimitExpiry, graphql_name='expiry')


class SponsorAndLifetimeValueOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorAndLifetimeValueOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorableOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorableOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorsActivityOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorsActivityOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorsTierOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorsTierOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorshipNewsletterOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipNewsletterOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorshipOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class StarOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(StarOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class StartOrganizationMigrationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'source_org_url', 'target_org_name', 'target_enterprise_id', 'source_access_token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    source_org_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='sourceOrgUrl')
    target_org_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetOrgName')
    target_enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='targetEnterpriseId')
    source_access_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAccessToken')


class StartRepositoryMigrationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'source_id', 'owner_id', 'source_repository_url', 'repository_name', 'continue_on_error', 'git_archive_url', 'metadata_archive_url', 'access_token', 'github_pat', 'skip_releases', 'target_repo_visibility', 'lock_source')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sourceId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    source_repository_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='sourceRepositoryUrl')
    repository_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repositoryName')
    continue_on_error = sgqlc.types.Field(Boolean, graphql_name='continueOnError')
    git_archive_url = sgqlc.types.Field(String, graphql_name='gitArchiveUrl')
    metadata_archive_url = sgqlc.types.Field(String, graphql_name='metadataArchiveUrl')
    access_token = sgqlc.types.Field(String, graphql_name='accessToken')
    github_pat = sgqlc.types.Field(String, graphql_name='githubPat')
    skip_releases = sgqlc.types.Field(Boolean, graphql_name='skipReleases')
    target_repo_visibility = sgqlc.types.Field(String, graphql_name='targetRepoVisibility')
    lock_source = sgqlc.types.Field(Boolean, graphql_name='lockSource')


class StatusCheckConfigurationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('context', 'integration_id')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')
    integration_id = sgqlc.types.Field(Int, graphql_name='integrationId')


class SubmitPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'pull_request_review_id', 'event', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(ID, graphql_name='pullRequestId')
    pull_request_review_id = sgqlc.types.Field(ID, graphql_name='pullRequestReviewId')
    event = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewEvent), graphql_name='event')
    body = sgqlc.types.Field(String, graphql_name='body')


class TagNamePatternParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(Boolean, graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class TeamDiscussionCommentOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionCommentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamDiscussionOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamMemberOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamRepositoryOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamRepositoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TransferEnterpriseOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id', 'destination_enterprise_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    destination_enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='destinationEnterpriseId')


class TransferIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id', 'repository_id', 'create_labels_if_missing')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    create_labels_if_missing = sgqlc.types.Field(Boolean, graphql_name='createLabelsIfMissing')


class UnarchiveProjectV2ItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'item_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')


class UnarchiveRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class UnfollowOrganizationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')


class UnfollowUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')


class UnlinkProjectV2FromRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class UnlinkProjectV2FromTeamInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'team_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='teamId')


class UnlinkRepositoryFromProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'repository_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')


class UnlockLockableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'lockable_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    lockable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='lockableId')


class UnmarkDiscussionCommentAsAnswerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UnmarkFileAsViewedInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'path')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')


class UnmarkIssueAsDuplicateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'duplicate_id', 'canonical_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    duplicate_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='duplicateId')
    canonical_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='canonicalId')


class UnmarkProjectV2AsTemplateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class UnminimizeCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')


class UnpinIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class UnresolveReviewThreadInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'thread_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='threadId')


class UpdateBranchProtectionRuleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'branch_protection_rule_id', 'pattern', 'requires_approving_reviews', 'required_approving_review_count', 'requires_commit_signatures', 'requires_linear_history', 'blocks_creations', 'allows_force_pushes', 'allows_deletions', 'is_admin_enforced', 'requires_status_checks', 'requires_strict_status_checks', 'requires_code_owner_reviews', 'dismisses_stale_reviews', 'restricts_review_dismissals', 'review_dismissal_actor_ids', 'bypass_pull_request_actor_ids', 'bypass_force_push_actor_ids', 'restricts_pushes', 'push_actor_ids', 'required_status_check_contexts', 'required_status_checks', 'requires_deployments', 'required_deployment_environments', 'requires_conversation_resolution', 'require_last_push_approval', 'lock_branch', 'lock_allows_fetch_and_merge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    branch_protection_rule_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='branchProtectionRuleId')
    pattern = sgqlc.types.Field(String, graphql_name='pattern')
    requires_approving_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresApprovingReviews')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    requires_commit_signatures = sgqlc.types.Field(Boolean, graphql_name='requiresCommitSignatures')
    requires_linear_history = sgqlc.types.Field(Boolean, graphql_name='requiresLinearHistory')
    blocks_creations = sgqlc.types.Field(Boolean, graphql_name='blocksCreations')
    allows_force_pushes = sgqlc.types.Field(Boolean, graphql_name='allowsForcePushes')
    allows_deletions = sgqlc.types.Field(Boolean, graphql_name='allowsDeletions')
    is_admin_enforced = sgqlc.types.Field(Boolean, graphql_name='isAdminEnforced')
    requires_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStatusChecks')
    requires_strict_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStrictStatusChecks')
    requires_code_owner_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresCodeOwnerReviews')
    dismisses_stale_reviews = sgqlc.types.Field(Boolean, graphql_name='dismissesStaleReviews')
    restricts_review_dismissals = sgqlc.types.Field(Boolean, graphql_name='restrictsReviewDismissals')
    review_dismissal_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='reviewDismissalActorIds')
    bypass_pull_request_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='bypassPullRequestActorIds')
    bypass_force_push_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='bypassForcePushActorIds')
    restricts_pushes = sgqlc.types.Field(Boolean, graphql_name='restrictsPushes')
    push_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='pushActorIds')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredStatusCheckContexts')
    required_status_checks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RequiredStatusCheckInput)), graphql_name='requiredStatusChecks')
    requires_deployments = sgqlc.types.Field(Boolean, graphql_name='requiresDeployments')
    required_deployment_environments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredDeploymentEnvironments')
    requires_conversation_resolution = sgqlc.types.Field(Boolean, graphql_name='requiresConversationResolution')
    require_last_push_approval = sgqlc.types.Field(Boolean, graphql_name='requireLastPushApproval')
    lock_branch = sgqlc.types.Field(Boolean, graphql_name='lockBranch')
    lock_allows_fetch_and_merge = sgqlc.types.Field(Boolean, graphql_name='lockAllowsFetchAndMerge')


class UpdateCheckRunInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'check_run_id', 'name', 'details_url', 'external_id', 'status', 'started_at', 'conclusion', 'completed_at', 'output', 'actions')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    check_run_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='checkRunId')
    name = sgqlc.types.Field(String, graphql_name='name')
    details_url = sgqlc.types.Field(URI, graphql_name='detailsUrl')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    status = sgqlc.types.Field(RequestableCheckStatusState, graphql_name='status')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    conclusion = sgqlc.types.Field(CheckConclusionState, graphql_name='conclusion')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    output = sgqlc.types.Field(CheckRunOutput, graphql_name='output')
    actions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CheckRunAction)), graphql_name='actions')


class UpdateCheckSuitePreferencesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'auto_trigger_preferences')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    auto_trigger_preferences = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CheckSuiteAutoTriggerPreference))), graphql_name='autoTriggerPreferences')


class UpdateDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='commentId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class UpdateDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion_id', 'title', 'body', 'category_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='discussionId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    category_id = sgqlc.types.Field(ID, graphql_name='categoryId')


class UpdateEnterpriseAdministratorRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'login', 'role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role')


class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value', 'policy_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    policy_value = sgqlc.types.Field(EnterpriseAllowPrivateRepositoryForkingPolicyValue, graphql_name='policyValue')


class UpdateEnterpriseDefaultRepositoryPermissionSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseDefaultRepositoryPermissionSettingValue), graphql_name='settingValue')


class UpdateEnterpriseDeployKeySettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value', 'members_can_create_repositories_policy_enabled', 'members_can_create_public_repositories', 'members_can_create_private_repositories', 'members_can_create_internal_repositories')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(EnterpriseMembersCanCreateRepositoriesSettingValue, graphql_name='settingValue')
    members_can_create_repositories_policy_enabled = sgqlc.types.Field(Boolean, graphql_name='membersCanCreateRepositoriesPolicyEnabled')
    members_can_create_public_repositories = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePublicRepositories')
    members_can_create_private_repositories = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePrivateRepositories')
    members_can_create_internal_repositories = sgqlc.types.Field(Boolean, graphql_name='membersCanCreateInternalRepositories')


class UpdateEnterpriseMembersCanDeleteIssuesSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanMakePurchasesSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMembersCanMakePurchasesSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseOrganizationProjectsSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseOwnerOrganizationRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'organization_id', 'organization_role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    organization_role = sgqlc.types.Field(sgqlc.types.non_null(RoleInOrganization), graphql_name='organizationRole')


class UpdateEnterpriseProfileInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'name', 'description', 'website_url', 'location', 'security_contact_email')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')
    location = sgqlc.types.Field(String, graphql_name='location')
    security_contact_email = sgqlc.types.Field(String, graphql_name='securityContactEmail')


class UpdateEnterpriseRepositoryProjectsSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseTeamDiscussionsSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')


class UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseDisallowedMethodsSettingValue), graphql_name='settingValue')


class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledSettingValue), graphql_name='settingValue')


class UpdateEnvironmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment_id', 'wait_timer', 'reviewers', 'prevent_self_review')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='environmentId')
    wait_timer = sgqlc.types.Field(Int, graphql_name='waitTimer')
    reviewers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='reviewers')
    prevent_self_review = sgqlc.types.Field(Boolean, graphql_name='preventSelfReview')


class UpdateIpAllowListEnabledSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListEnabledSettingValue), graphql_name='settingValue')


class UpdateIpAllowListEntryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ip_allow_list_entry_id', 'allow_list_value', 'name', 'is_active')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ip_allow_list_entry_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ipAllowListEntryId')
    allow_list_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='allowListValue')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')


class UpdateIpAllowListForInstalledAppsEnabledSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListForInstalledAppsEnabledSettingValue), graphql_name='settingValue')


class UpdateIssueCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class UpdateIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'title', 'body', 'assignee_ids', 'milestone_id', 'label_ids', 'state', 'project_ids', 'issue_type_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')
    milestone_id = sgqlc.types.Field(ID, graphql_name='milestoneId')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    state = sgqlc.types.Field(IssueState, graphql_name='state')
    project_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectIds')
    issue_type_id = sgqlc.types.Field(ID, graphql_name='issueTypeId')


class UpdateIssueIssueTypeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_type_id', 'issue_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_type_id = sgqlc.types.Field(ID, graphql_name='issueTypeId')
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')


class UpdateIssueTypeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_type_id', 'is_enabled', 'name', 'description', 'color')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueTypeId')
    is_enabled = sgqlc.types.Field(Boolean, graphql_name='isEnabled')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    color = sgqlc.types.Field(IssueTypeColor, graphql_name='color')


class UpdateLabelInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'color', 'description', 'name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateNotificationRestrictionSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner_id', 'setting_value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(NotificationRestrictionSettingValue), graphql_name='settingValue')


class UpdateOrganizationAllowPrivateRepositoryForkingSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id', 'forking_enabled')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    forking_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='forkingEnabled')


class UpdateOrganizationWebCommitSignoffSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization_id', 'web_commit_signoff_required')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    web_commit_signoff_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webCommitSignoffRequired')


class UpdateParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('update_allows_fetch_and_merge',)
    update_allows_fetch_and_merge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAllowsFetchAndMerge')


class UpdatePatreonSponsorabilityInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsorable_login', 'enable_patreon_sponsorships')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')
    enable_patreon_sponsorships = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enablePatreonSponsorships')


class UpdateProjectCardInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_card_id', 'is_archived', 'note')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectCardId')
    is_archived = sgqlc.types.Field(Boolean, graphql_name='isArchived')
    note = sgqlc.types.Field(String, graphql_name='note')


class UpdateProjectColumnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_column_id', 'name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectColumnId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class UpdateProjectInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'name', 'body', 'state', 'public')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(String, graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    state = sgqlc.types.Field(ProjectState, graphql_name='state')
    public = sgqlc.types.Field(Boolean, graphql_name='public')


class UpdateProjectV2CollaboratorsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'collaborators')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    collaborators = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectV2Collaborator))), graphql_name='collaborators')


class UpdateProjectV2DraftIssueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'draft_issue_id', 'title', 'body', 'assignee_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    draft_issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='draftIssueId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')


class UpdateProjectV2FieldInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'field_id', 'name', 'single_select_options', 'iteration_configuration')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    field_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fieldId')
    name = sgqlc.types.Field(String, graphql_name='name')
    single_select_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProjectV2SingleSelectFieldOptionInput)), graphql_name='singleSelectOptions')
    iteration_configuration = sgqlc.types.Field(ProjectV2IterationFieldConfigurationInput, graphql_name='iterationConfiguration')


class UpdateProjectV2Input(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'title', 'short_description', 'readme', 'closed', 'public')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    title = sgqlc.types.Field(String, graphql_name='title')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')
    readme = sgqlc.types.Field(String, graphql_name='readme')
    closed = sgqlc.types.Field(Boolean, graphql_name='closed')
    public = sgqlc.types.Field(Boolean, graphql_name='public')


class UpdateProjectV2ItemFieldValueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'item_id', 'field_id', 'value')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')
    field_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fieldId')
    value = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2FieldValue), graphql_name='value')


class UpdateProjectV2ItemPositionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_id', 'item_id', 'after_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')
    after_id = sgqlc.types.Field(ID, graphql_name='afterId')


class UpdateProjectV2StatusUpdateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'status_update_id', 'start_date', 'target_date', 'status', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    status_update_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='statusUpdateId')
    start_date = sgqlc.types.Field(Date, graphql_name='startDate')
    target_date = sgqlc.types.Field(Date, graphql_name='targetDate')
    status = sgqlc.types.Field(ProjectV2StatusUpdateStatus, graphql_name='status')
    body = sgqlc.types.Field(String, graphql_name='body')


class UpdatePullRequestBranchInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'expected_head_oid', 'update_method')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    expected_head_oid = sgqlc.types.Field(GitObjectID, graphql_name='expectedHeadOid')
    update_method = sgqlc.types.Field(PullRequestBranchUpdateMethod, graphql_name='updateMethod')


class UpdatePullRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_id', 'base_ref_name', 'title', 'body', 'state', 'maintainer_can_modify', 'assignee_ids', 'milestone_id', 'label_ids', 'project_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    base_ref_name = sgqlc.types.Field(String, graphql_name='baseRefName')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    state = sgqlc.types.Field(PullRequestUpdateState, graphql_name='state')
    maintainer_can_modify = sgqlc.types.Field(Boolean, graphql_name='maintainerCanModify')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')
    milestone_id = sgqlc.types.Field(ID, graphql_name='milestoneId')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    project_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectIds')


class UpdatePullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review_comment_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_comment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewCommentId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class UpdatePullRequestReviewInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review_id', 'body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class UpdateRefInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ref_id', 'oid', 'force')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ref_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='refId')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    force = sgqlc.types.Field(Boolean, graphql_name='force')


class UpdateRefsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'ref_updates')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    ref_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RefUpdate))), graphql_name='refUpdates')


class UpdateRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'name', 'description', 'template', 'homepage_url', 'has_wiki_enabled', 'has_issues_enabled', 'has_projects_enabled', 'has_discussions_enabled', 'has_sponsorships_enabled')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    template = sgqlc.types.Field(Boolean, graphql_name='template')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    has_wiki_enabled = sgqlc.types.Field(Boolean, graphql_name='hasWikiEnabled')
    has_issues_enabled = sgqlc.types.Field(Boolean, graphql_name='hasIssuesEnabled')
    has_projects_enabled = sgqlc.types.Field(Boolean, graphql_name='hasProjectsEnabled')
    has_discussions_enabled = sgqlc.types.Field(Boolean, graphql_name='hasDiscussionsEnabled')
    has_sponsorships_enabled = sgqlc.types.Field(Boolean, graphql_name='hasSponsorshipsEnabled')


class UpdateRepositoryRulesetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_ruleset_id', 'name', 'target', 'rules', 'conditions', 'enforcement', 'bypass_actors')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_ruleset_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryRulesetId')
    name = sgqlc.types.Field(String, graphql_name='name')
    target = sgqlc.types.Field(RepositoryRulesetTarget, graphql_name='target')
    rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryRuleInput)), graphql_name='rules')
    conditions = sgqlc.types.Field(RepositoryRuleConditionsInput, graphql_name='conditions')
    enforcement = sgqlc.types.Field(RuleEnforcement, graphql_name='enforcement')
    bypass_actors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryRulesetBypassActorInput)), graphql_name='bypassActors')


class UpdateRepositoryWebCommitSignoffSettingInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'web_commit_signoff_required')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    web_commit_signoff_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webCommitSignoffRequired')


class UpdateSponsorshipPreferencesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsor_id', 'sponsor_login', 'sponsorable_id', 'sponsorable_login', 'receive_emails', 'privacy_level')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsor_id = sgqlc.types.Field(ID, graphql_name='sponsorId')
    sponsor_login = sgqlc.types.Field(String, graphql_name='sponsorLogin')
    sponsorable_id = sgqlc.types.Field(ID, graphql_name='sponsorableId')
    sponsorable_login = sgqlc.types.Field(String, graphql_name='sponsorableLogin')
    receive_emails = sgqlc.types.Field(Boolean, graphql_name='receiveEmails')
    privacy_level = sgqlc.types.Field(SponsorshipPrivacy, graphql_name='privacyLevel')


class UpdateSubscriptionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subscribable_id', 'state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subscribable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subscribableId')
    state = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='state')


class UpdateTeamDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'body', 'body_version')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_version = sgqlc.types.Field(String, graphql_name='bodyVersion')


class UpdateTeamDiscussionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'title', 'body', 'body_version', 'pinned')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_version = sgqlc.types.Field(String, graphql_name='bodyVersion')
    pinned = sgqlc.types.Field(Boolean, graphql_name='pinned')


class UpdateTeamReviewAssignmentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'enabled', 'algorithm', 'team_member_count', 'notify_team', 'remove_team_request', 'include_child_team_members', 'count_members_already_requested', 'excluded_team_member_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    algorithm = sgqlc.types.Field(TeamReviewAssignmentAlgorithm, graphql_name='algorithm')
    team_member_count = sgqlc.types.Field(Int, graphql_name='teamMemberCount')
    notify_team = sgqlc.types.Field(Boolean, graphql_name='notifyTeam')
    remove_team_request = sgqlc.types.Field(Boolean, graphql_name='removeTeamRequest')
    include_child_team_members = sgqlc.types.Field(Boolean, graphql_name='includeChildTeamMembers')
    count_members_already_requested = sgqlc.types.Field(Boolean, graphql_name='countMembersAlreadyRequested')
    excluded_team_member_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='excludedTeamMemberIds')


class UpdateTeamsRepositoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'team_ids', 'permission')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    team_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='teamIds')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')


class UpdateTopicsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_id', 'topic_names')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    topic_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='topicNames')


class UpdateUserListInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'list_id', 'name', 'description', 'is_private')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    list_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='listId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_private = sgqlc.types.Field(Boolean, graphql_name='isPrivate')


class UpdateUserListsForItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item_id', 'list_ids', 'suggested_list_ids')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='itemId')
    list_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='listIds')
    suggested_list_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='suggestedListIds')


class UserStatusOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(UserStatusOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class VerifiableDomainOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(VerifiableDomainOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class VerifyVerifiableDomainInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class WorkflowFileReferenceInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('path', 'ref', 'repository_id', 'sha')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    ref = sgqlc.types.Field(String, graphql_name='ref')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryId')
    sha = sgqlc.types.Field(String, graphql_name='sha')


class WorkflowRunOrder(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'direction')
    field = sgqlc.types.Field(sgqlc.types.non_null(WorkflowRunOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class WorkflowsParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('do_not_enforce_on_create', 'workflows')
    do_not_enforce_on_create = sgqlc.types.Field(Boolean, graphql_name='doNotEnforceOnCreate')
    workflows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkflowFileReferenceInput))), graphql_name='workflows')



########################################################################
# Output Objects and Interfaces
########################################################################
class Actor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('avatar_url', 'login', 'resource_path', 'url')
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Assignable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('assigned_actors', 'assignees', 'suggested_actors')
    assigned_actors = sgqlc.types.Field(sgqlc.types.non_null('AssigneeConnection'), graphql_name='assignedActors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    assignees = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    suggested_actors = sgqlc.types.Field(sgqlc.types.non_null('AssigneeConnection'), graphql_name='suggestedActors', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class AuditEntry(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ()


class Closable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('closed', 'closed_at', 'viewer_can_close', 'viewer_can_reopen')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    viewer_can_close = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanClose')
    viewer_can_reopen = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReopen')


class Comment(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('author', 'author_association', 'body', 'body_html', 'body_text', 'created_at', 'created_via_email', 'editor', 'id', 'includes_created_edit', 'last_edited_at', 'published_at', 'updated_at', 'user_content_edits', 'viewer_did_author')
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_content_edits = sgqlc.types.Field('UserContentEditConnection', graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class Contribution(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('is_restricted', 'occurred_at', 'resource_path', 'url', 'user')
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class Deletable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('viewer_can_delete',)
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')


class EnterpriseAuditEntryData(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('enterprise_resource_path', 'enterprise_slug', 'enterprise_url')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')


class GitObject(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('abbreviated_oid', 'commit_resource_path', 'commit_url', 'id', 'oid', 'repository')
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class GitSignature(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('email', 'is_valid', 'payload', 'signature', 'signer', 'state', 'verified_at', 'was_signed_by_git_hub')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field('User', graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')
    verified_at = sgqlc.types.Field(DateTime, graphql_name='verifiedAt')
    was_signed_by_git_hub = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasSignedByGitHub')


class HovercardContext(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('message', 'octicon')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')


class Labelable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('labels', 'viewer_can_label')
    labels = sgqlc.types.Field('LabelConnection', graphql_name='labels', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(LabelOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanLabel')


class Lockable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('active_lock_reason', 'locked')
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')


class MemberStatusable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('member_statuses',)
    member_statuses = sgqlc.types.Field(sgqlc.types.non_null('UserStatusConnection'), graphql_name='memberStatuses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(UserStatusOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )


class Migration(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('continue_on_error', 'created_at', 'database_id', 'failure_reason', 'id', 'migration_log_url', 'migration_source', 'repository_name', 'source_url', 'state', 'warnings_count')
    continue_on_error = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='continueOnError')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(String, graphql_name='databaseId')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    migration_log_url = sgqlc.types.Field(URI, graphql_name='migrationLogUrl')
    migration_source = sgqlc.types.Field(sgqlc.types.non_null('MigrationSource'), graphql_name='migrationSource')
    repository_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repositoryName')
    source_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='sourceUrl')
    state = sgqlc.types.Field(sgqlc.types.non_null(MigrationState), graphql_name='state')
    warnings_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='warningsCount')


class Minimizable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('is_minimized', 'minimized_reason', 'viewer_can_minimize', 'viewer_can_unminimize')
    is_minimized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMinimized')
    minimized_reason = sgqlc.types.Field(String, graphql_name='minimizedReason')
    viewer_can_minimize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMinimize')
    viewer_can_unminimize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUnminimize')


class Node(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OauthApplicationAuditEntryData(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('oauth_application_name', 'oauth_application_resource_path', 'oauth_application_url')
    oauth_application_name = sgqlc.types.Field(String, graphql_name='oauthApplicationName')
    oauth_application_resource_path = sgqlc.types.Field(URI, graphql_name='oauthApplicationResourcePath')
    oauth_application_url = sgqlc.types.Field(URI, graphql_name='oauthApplicationUrl')


class OrganizationAuditEntryData(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ()


class PackageOwner(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'packages')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    packages = sgqlc.types.Field(sgqlc.types.non_null('PackageConnection'), graphql_name='packages', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='names', default=None)),
        ('repository_id', sgqlc.types.Arg(ID, graphql_name='repositoryId', default=None)),
        ('package_type', sgqlc.types.Arg(PackageType, graphql_name='packageType', default=None)),
        ('order_by', sgqlc.types.Arg(PackageOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
))
    )


class ProfileOwner(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('any_pinnable_items', 'email', 'id', 'item_showcase', 'location', 'login', 'name', 'pinnable_items', 'pinned_items', 'pinned_items_remaining', 'viewer_can_change_pinned_items', 'website_url')
    any_pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='anyPinnableItems', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(PinnableItemType, graphql_name='type', default=None)),
))
    )
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    item_showcase = sgqlc.types.Field(sgqlc.types.non_null('ProfileItemShowcase'), graphql_name='itemShowcase')
    location = sgqlc.types.Field(String, graphql_name='location')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    name = sgqlc.types.Field(String, graphql_name='name')
    pinnable_items = sgqlc.types.Field(sgqlc.types.non_null('PinnableItemConnection'), graphql_name='pinnableItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items = sgqlc.types.Field(sgqlc.types.non_null('PinnableItemConnection'), graphql_name='pinnedItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pinnedItemsRemaining')
    viewer_can_change_pinned_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanChangePinnedItems')
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class ProjectOwner(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ()


class ProjectV2Event(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('project', 'was_automated')
    project = sgqlc.types.Field('ProjectV2', graphql_name='project')
    was_automated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasAutomated')


class ProjectV2FieldCommon(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('created_at', 'data_type', 'database_id', 'id', 'name', 'project', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    data_type = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2FieldType), graphql_name='dataType')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    project = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2'), graphql_name='project')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class ProjectV2ItemFieldValueCommon(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('created_at', 'creator', 'database_id', 'field', 'id', 'item', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2Item'), graphql_name='item')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class ProjectV2Owner(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'project_v2', 'projects_v2')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects_v2 = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2Connection'), graphql_name='projectsV2', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2Order, graphql_name='orderBy', default={'field': 'NUMBER', 'direction': 'DESC'})),
        ('min_permission_level', sgqlc.types.Arg(ProjectV2PermissionLevel, graphql_name='minPermissionLevel', default='READ')),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ProjectV2Recent(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('recent_projects',)
    recent_projects = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2Connection'), graphql_name='recentProjects', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class Reactable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('database_id', 'id', 'reaction_groups', 'reactions', 'viewer_can_react')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionGroup')), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null('ReactionConnection'), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')


class RepositoryAuditEntryData(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('repository', 'repository_name', 'repository_resource_path', 'repository_url')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')


class RepositoryDiscussionAuthor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('repository_discussions',)
    repository_discussions = sgqlc.types.Field(sgqlc.types.non_null('DiscussionConnection'), graphql_name='repositoryDiscussions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(DiscussionOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('repository_id', sgqlc.types.Arg(ID, graphql_name='repositoryId', default=None)),
        ('answered', sgqlc.types.Arg(Boolean, graphql_name='answered', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(DiscussionState)), graphql_name='states', default=())),
))
    )


class RepositoryDiscussionCommentAuthor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('repository_discussion_comments',)
    repository_discussion_comments = sgqlc.types.Field(sgqlc.types.non_null('DiscussionCommentConnection'), graphql_name='repositoryDiscussionComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_id', sgqlc.types.Arg(ID, graphql_name='repositoryId', default=None)),
        ('only_answers', sgqlc.types.Arg(Boolean, graphql_name='onlyAnswers', default=False)),
))
    )


class RepositoryInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('archived_at', 'created_at', 'description', 'description_html', 'fork_count', 'has_discussions_enabled', 'has_issues_enabled', 'has_projects_enabled', 'has_sponsorships_enabled', 'has_wiki_enabled', 'homepage_url', 'is_archived', 'is_fork', 'is_in_organization', 'is_locked', 'is_mirror', 'is_private', 'is_template', 'license_info', 'lock_reason', 'mirror_url', 'name', 'name_with_owner', 'open_graph_image_url', 'owner', 'pushed_at', 'resource_path', 'short_description_html', 'updated_at', 'url', 'uses_custom_open_graph_image', 'visibility')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forkCount')
    has_discussions_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDiscussionsEnabled')
    has_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIssuesEnabled')
    has_projects_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasProjectsEnabled')
    has_sponsorships_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasSponsorshipsEnabled')
    has_wiki_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWikiEnabled')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_in_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInOrganization')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_mirror = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMirror')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    is_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplate')
    license_info = sgqlc.types.Field('License', graphql_name='licenseInfo')
    lock_reason = sgqlc.types.Field(RepositoryLockReason, graphql_name='lockReason')
    mirror_url = sgqlc.types.Field(URI, graphql_name='mirrorUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    open_graph_image_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='openGraphImageUrl')
    owner = sgqlc.types.Field(sgqlc.types.non_null('RepositoryOwner'), graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=200)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    uses_custom_open_graph_image = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='usesCustomOpenGraphImage')
    visibility = sgqlc.types.Field(sgqlc.types.non_null(RepositoryVisibility), graphql_name='visibility')


class RepositoryNode(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('repository',)
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class RepositoryOwner(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('avatar_url', 'id', 'login', 'repositories', 'repository', 'resource_path', 'url')
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    repositories = sgqlc.types.Field(sgqlc.types.non_null('RepositoryConnection'), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('visibility', sgqlc.types.Arg(RepositoryVisibility, graphql_name='visibility', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=('OWNER', 'COLLABORATOR'))),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('has_issues_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasIssuesEnabled', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_archived', sgqlc.types.Arg(Boolean, graphql_name='isArchived', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('follow_renames', sgqlc.types.Arg(Boolean, graphql_name='followRenames', default=True)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RequirableByPullRequest(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('is_required',)
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired', args=sgqlc.types.ArgDict((
        ('pull_request_id', sgqlc.types.Arg(ID, graphql_name='pullRequestId', default=None)),
        ('pull_request_number', sgqlc.types.Arg(Int, graphql_name='pullRequestNumber', default=None)),
))
    )


class Sponsorable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('estimated_next_sponsors_payout_in_cents', 'has_sponsors_listing', 'is_sponsored_by', 'is_sponsoring_viewer', 'lifetime_received_sponsorship_values', 'monthly_estimated_sponsors_income_in_cents', 'sponsoring', 'sponsors', 'sponsors_activities', 'sponsors_listing', 'sponsorship_for_viewer_as_sponsor', 'sponsorship_for_viewer_as_sponsorable', 'sponsorship_newsletters', 'sponsorships_as_maintainer', 'sponsorships_as_sponsor', 'total_sponsorship_amount_as_sponsor_in_cents', 'viewer_can_sponsor', 'viewer_is_sponsoring')
    estimated_next_sponsors_payout_in_cents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='estimatedNextSponsorsPayoutInCents')
    has_sponsors_listing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasSponsorsListing')
    is_sponsored_by = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSponsoredBy', args=sgqlc.types.ArgDict((
        ('account_login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='accountLogin', default=None)),
))
    )
    is_sponsoring_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSponsoringViewer')
    lifetime_received_sponsorship_values = sgqlc.types.Field(sgqlc.types.non_null('SponsorAndLifetimeValueConnection'), graphql_name='lifetimeReceivedSponsorshipValues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorAndLifetimeValueOrder, graphql_name='orderBy', default={'field': 'SPONSOR_LOGIN', 'direction': 'ASC'})),
))
    )
    monthly_estimated_sponsors_income_in_cents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='monthlyEstimatedSponsorsIncomeInCents')
    sponsoring = sgqlc.types.Field(sgqlc.types.non_null('SponsorConnection'), graphql_name='sponsoring', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorOrder, graphql_name='orderBy', default={'field': 'RELEVANCE', 'direction': 'DESC'})),
))
    )
    sponsors = sgqlc.types.Field(sgqlc.types.non_null('SponsorConnection'), graphql_name='sponsors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('tier_id', sgqlc.types.Arg(ID, graphql_name='tierId', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorOrder, graphql_name='orderBy', default={'field': 'RELEVANCE', 'direction': 'DESC'})),
))
    )
    sponsors_activities = sgqlc.types.Field(sgqlc.types.non_null('SponsorsActivityConnection'), graphql_name='sponsorsActivities', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('period', sgqlc.types.Arg(SponsorsActivityPeriod, graphql_name='period', default='MONTH')),
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('until', sgqlc.types.Arg(DateTime, graphql_name='until', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorsActivityOrder, graphql_name='orderBy', default={'field': 'TIMESTAMP', 'direction': 'DESC'})),
        ('actions', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SponsorsActivityAction)), graphql_name='actions', default=())),
        ('include_as_sponsor', sgqlc.types.Arg(Boolean, graphql_name='includeAsSponsor', default=False)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=True)),
))
    )
    sponsors_listing = sgqlc.types.Field('SponsorsListing', graphql_name='sponsorsListing')
    sponsorship_for_viewer_as_sponsor = sgqlc.types.Field('Sponsorship', graphql_name='sponsorshipForViewerAsSponsor', args=sgqlc.types.ArgDict((
        ('active_only', sgqlc.types.Arg(Boolean, graphql_name='activeOnly', default=True)),
))
    )
    sponsorship_for_viewer_as_sponsorable = sgqlc.types.Field('Sponsorship', graphql_name='sponsorshipForViewerAsSponsorable', args=sgqlc.types.ArgDict((
        ('active_only', sgqlc.types.Arg(Boolean, graphql_name='activeOnly', default=True)),
))
    )
    sponsorship_newsletters = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipNewsletterConnection'), graphql_name='sponsorshipNewsletters', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorshipNewsletterOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
))
    )
    sponsorships_as_maintainer = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipConnection'), graphql_name='sponsorshipsAsMaintainer', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=False)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
        ('active_only', sgqlc.types.Arg(Boolean, graphql_name='activeOnly', default=True)),
))
    )
    sponsorships_as_sponsor = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipConnection'), graphql_name='sponsorshipsAsSponsor', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
        ('maintainer_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='maintainerLogins', default=None)),
        ('active_only', sgqlc.types.Arg(Boolean, graphql_name='activeOnly', default=True)),
))
    )
    total_sponsorship_amount_as_sponsor_in_cents = sgqlc.types.Field(Int, graphql_name='totalSponsorshipAmountAsSponsorInCents', args=sgqlc.types.ArgDict((
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('until', sgqlc.types.Arg(DateTime, graphql_name='until', default=None)),
        ('sponsorable_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='sponsorableLogins', default=())),
))
    )
    viewer_can_sponsor = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSponsor')
    viewer_is_sponsoring = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsSponsoring')


class Starrable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'stargazer_count', 'stargazers', 'viewer_has_starred')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    stargazer_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stargazerCount')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null('StargazerConnection'), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')


class Subscribable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'viewer_can_subscribe', 'viewer_subscription')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')


class SubscribableThread(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'viewer_thread_subscription_form_action', 'viewer_thread_subscription_status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    viewer_thread_subscription_form_action = sgqlc.types.Field(ThreadSubscriptionFormAction, graphql_name='viewerThreadSubscriptionFormAction')
    viewer_thread_subscription_status = sgqlc.types.Field(ThreadSubscriptionState, graphql_name='viewerThreadSubscriptionStatus')


class TeamAuditEntryData(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('team', 'team_name', 'team_resource_path', 'team_url')
    team = sgqlc.types.Field('Team', graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')


class TopicAuditEntryData(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('topic', 'topic_name')
    topic = sgqlc.types.Field('Topic', graphql_name='topic')
    topic_name = sgqlc.types.Field(String, graphql_name='topicName')


class UniformResourceLocatable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('resource_path', 'url')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Updatable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('viewer_can_update',)
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')


class UpdatableComment(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('viewer_cannot_update_reasons',)
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')


class Votable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('upvote_count', 'viewer_can_upvote', 'viewer_has_upvoted')
    upvote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='upvoteCount')
    viewer_can_upvote = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpvote')
    viewer_has_upvoted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasUpvoted')


class AbortQueuedMigrationsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class AbortRepositoryMigrationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class AcceptEnterpriseAdministratorInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='invitation')
    message = sgqlc.types.Field(String, graphql_name='message')


class AcceptEnterpriseMemberInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseMemberInvitation', graphql_name='invitation')
    message = sgqlc.types.Field(String, graphql_name='message')


class AcceptTopicSuggestionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AccessUserNamespaceRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'expires_at', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class ActorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ActorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(Actor), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ActorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(Actor, graphql_name='node')


class ActorLocation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('city', 'country', 'country_code', 'region', 'region_code')
    city = sgqlc.types.Field(String, graphql_name='city')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    region = sgqlc.types.Field(String, graphql_name='region')
    region_code = sgqlc.types.Field(String, graphql_name='regionCode')


class AddAssigneesToAssignablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assignable', 'client_mutation_id')
    assignable = sgqlc.types.Field(Assignable, graphql_name='assignable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddBlockedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('blocking_issue', 'client_mutation_id', 'issue')
    blocking_issue = sgqlc.types.Field('Issue', graphql_name='blockingIssue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class AddCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment_edge', 'subject', 'timeline_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_edge = sgqlc.types.Field('IssueCommentEdge', graphql_name='commentEdge')
    subject = sgqlc.types.Field(Node, graphql_name='subject')
    timeline_edge = sgqlc.types.Field('IssueTimelineItemEdge', graphql_name='timelineEdge')


class AddDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('DiscussionComment', graphql_name='comment')


class AddDiscussionPollVotePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'poll_option')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    poll_option = sgqlc.types.Field('DiscussionPollOption', graphql_name='pollOption')


class AddEnterpriseOrganizationMemberPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'users')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='users')


class AddEnterpriseSupportEntitlementPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')


class AddLabelsToLabelablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'labelable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable = sgqlc.types.Field(Labelable, graphql_name='labelable')


class AddProjectCardPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('card_edge', 'client_mutation_id', 'project_column')
    card_edge = sgqlc.types.Field('ProjectCardEdge', graphql_name='cardEdge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column = sgqlc.types.Field('ProjectColumn', graphql_name='projectColumn')


class AddProjectColumnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'column_edge', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_edge = sgqlc.types.Field('ProjectColumnEdge', graphql_name='columnEdge')
    project = sgqlc.types.Field('Project', graphql_name='project')


class AddProjectV2DraftIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_item = sgqlc.types.Field('ProjectV2Item', graphql_name='projectItem')


class AddProjectV2ItemByIdPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item = sgqlc.types.Field('ProjectV2Item', graphql_name='item')


class AddPullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment', 'comment_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('PullRequestReviewComment', graphql_name='comment')
    comment_edge = sgqlc.types.Field('PullRequestReviewCommentEdge', graphql_name='commentEdge')


class AddPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review', 'review_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')
    review_edge = sgqlc.types.Field('PullRequestReviewEdge', graphql_name='reviewEdge')


class AddPullRequestReviewThreadPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'thread')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread = sgqlc.types.Field('PullRequestReviewThread', graphql_name='thread')


class AddPullRequestReviewThreadReplyPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('PullRequestReviewComment', graphql_name='comment')


class AddReactionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'reaction', 'reaction_groups', 'subject')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    reaction = sgqlc.types.Field('Reaction', graphql_name='reaction')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionGroup')), graphql_name='reactionGroups')
    subject = sgqlc.types.Field(Reactable, graphql_name='subject')


class AddStarPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'starrable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable = sgqlc.types.Field(Starrable, graphql_name='starrable')


class AddSubIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue', 'sub_issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    sub_issue = sgqlc.types.Field('Issue', graphql_name='subIssue')


class AddUpvotePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject = sgqlc.types.Field(Votable, graphql_name='subject')


class AddVerifiableDomainPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'domain')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    domain = sgqlc.types.Field('VerifiableDomain', graphql_name='domain')


class AnnouncementBanner(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('created_at', 'expires_at', 'is_user_dismissible', 'message')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    is_user_dismissible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUserDismissible')
    message = sgqlc.types.Field(String, graphql_name='message')


class ApproveDeploymentsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deployments')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deployments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Deployment')), graphql_name='deployments')


class ApproveVerifiableDomainPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'domain')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    domain = sgqlc.types.Field('VerifiableDomain', graphql_name='domain')


class ArchiveProjectV2ItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item = sgqlc.types.Field('ProjectV2Item', graphql_name='item')


class ArchiveRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class AssigneeConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('AssigneeEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Assignee'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AssigneeEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Assignee', graphql_name='node')


class AutoMergeRequest(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('author_email', 'commit_body', 'commit_headline', 'enabled_at', 'enabled_by', 'merge_method', 'pull_request')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    commit_body = sgqlc.types.Field(String, graphql_name='commitBody')
    commit_headline = sgqlc.types.Field(String, graphql_name='commitHeadline')
    enabled_at = sgqlc.types.Field(DateTime, graphql_name='enabledAt')
    enabled_by = sgqlc.types.Field(Actor, graphql_name='enabledBy')
    merge_method = sgqlc.types.Field(sgqlc.types.non_null(PullRequestMergeMethod), graphql_name='mergeMethod')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class Blame(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('ranges',)
    ranges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BlameRange'))), graphql_name='ranges')


class BlameRange(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('age', 'commit', 'ending_line', 'starting_line')
    age = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='age')
    commit = sgqlc.types.Field(sgqlc.types.non_null('Commit'), graphql_name='commit')
    ending_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endingLine')
    starting_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startingLine')


class BranchNamePatternParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class BranchProtectionRuleConflict(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('branch_protection_rule', 'conflicting_branch_protection_rule', 'ref')
    branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='branchProtectionRule')
    conflicting_branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='conflictingBranchProtectionRule')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class BranchProtectionRuleConflictConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('BranchProtectionRuleConflictEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(BranchProtectionRuleConflict), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BranchProtectionRuleConflictEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(BranchProtectionRuleConflict, graphql_name='node')


class BranchProtectionRuleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('BranchProtectionRuleEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('BranchProtectionRule'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BranchProtectionRuleEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('BranchProtectionRule', graphql_name='node')


class BypassForcePushAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('BypassForcePushAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('BypassForcePushAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BypassForcePushAllowanceEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('BypassForcePushAllowance', graphql_name='node')


class BypassPullRequestAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('BypassPullRequestAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('BypassPullRequestAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BypassPullRequestAllowanceEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('BypassPullRequestAllowance', graphql_name='node')


class CVSS(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('score', 'vector_string')
    score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='score')
    vector_string = sgqlc.types.Field(String, graphql_name='vectorString')


class CWEConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CWEEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CWE'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CWEEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CWE', graphql_name='node')


class CancelEnterpriseAdminInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='invitation')
    message = sgqlc.types.Field(String, graphql_name='message')


class CancelEnterpriseMemberInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseMemberInvitation', graphql_name='invitation')
    message = sgqlc.types.Field(String, graphql_name='message')


class CancelSponsorshipPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsors_tier')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsors_tier = sgqlc.types.Field('SponsorsTier', graphql_name='sponsorsTier')


class ChangeUserStatusPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'status')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    status = sgqlc.types.Field('UserStatus', graphql_name='status')


class CheckAnnotation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('annotation_level', 'blob_url', 'database_id', 'location', 'message', 'path', 'raw_details', 'title')
    annotation_level = sgqlc.types.Field(CheckAnnotationLevel, graphql_name='annotationLevel')
    blob_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='blobUrl')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    location = sgqlc.types.Field(sgqlc.types.non_null('CheckAnnotationSpan'), graphql_name='location')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    raw_details = sgqlc.types.Field(String, graphql_name='rawDetails')
    title = sgqlc.types.Field(String, graphql_name='title')


class CheckAnnotationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CheckAnnotationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(CheckAnnotation), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CheckAnnotationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(CheckAnnotation, graphql_name='node')


class CheckAnnotationPosition(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('column', 'line')
    column = sgqlc.types.Field(Int, graphql_name='column')
    line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='line')


class CheckAnnotationSpan(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(sgqlc.types.non_null(CheckAnnotationPosition), graphql_name='end')
    start = sgqlc.types.Field(sgqlc.types.non_null(CheckAnnotationPosition), graphql_name='start')


class CheckRunConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CheckRunEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CheckRun'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CheckRunEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CheckRun', graphql_name='node')


class CheckRunStateCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('count', 'state')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    state = sgqlc.types.Field(sgqlc.types.non_null(CheckRunState), graphql_name='state')


class CheckStep(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('completed_at', 'conclusion', 'external_id', 'name', 'number', 'seconds_to_completion', 'started_at', 'status')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    conclusion = sgqlc.types.Field(CheckConclusionState, graphql_name='conclusion')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    seconds_to_completion = sgqlc.types.Field(Int, graphql_name='secondsToCompletion')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(CheckStatusState), graphql_name='status')


class CheckStepConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CheckStepEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(CheckStep), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CheckStepEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(CheckStep, graphql_name='node')


class CheckSuiteConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CheckSuiteEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CheckSuite'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CheckSuiteEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CheckSuite', graphql_name='node')


class ClearLabelsFromLabelablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'labelable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable = sgqlc.types.Field(Labelable, graphql_name='labelable')


class ClearProjectV2ItemFieldValuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2_item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2_item = sgqlc.types.Field('ProjectV2Item', graphql_name='projectV2Item')


class CloneProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'job_status_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    job_status_id = sgqlc.types.Field(String, graphql_name='jobStatusId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class CloneTemplateRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class CloseDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class CloseIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class ClosePullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class CodeScanningParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('code_scanning_tools',)
    code_scanning_tools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CodeScanningTool'))), graphql_name='codeScanningTools')


class CodeScanningTool(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('alerts_threshold', 'security_alerts_threshold', 'tool')
    alerts_threshold = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alertsThreshold')
    security_alerts_threshold = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='securityAlertsThreshold')
    tool = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tool')


class CommitAuthorEmailPatternParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class CommitCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CommitCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CommitComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitCommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CommitComment', graphql_name='node')


class CommitConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CommitEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitContributionsByRepository(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('contributions', 'repository', 'resource_path', 'url')
    contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedCommitContributionConnection'), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(CommitContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class CommitEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Commit', graphql_name='node')


class CommitHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of(CommitEdge), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitMessagePatternParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class CommitterEmailPatternParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class ComparisonCommitConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('author_count', 'edges', 'nodes', 'page_info', 'total_count')
    author_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='authorCount')
    edges = sgqlc.types.Field(sgqlc.types.list_of(CommitEdge), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ContributingGuidelines(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('body', 'resource_path', 'url')
    body = sgqlc.types.Field(String, graphql_name='body')
    resource_path = sgqlc.types.Field(URI, graphql_name='resourcePath')
    url = sgqlc.types.Field(URI, graphql_name='url')


class ContributionCalendar(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('colors', 'is_halloween', 'months', 'total_contributions', 'weeks')
    colors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='colors')
    is_halloween = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHalloween')
    months = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContributionCalendarMonth'))), graphql_name='months')
    total_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalContributions')
    weeks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContributionCalendarWeek'))), graphql_name='weeks')


class ContributionCalendarDay(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('color', 'contribution_count', 'contribution_level', 'date', 'weekday')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    contribution_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='contributionCount')
    contribution_level = sgqlc.types.Field(sgqlc.types.non_null(ContributionLevel), graphql_name='contributionLevel')
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weekday')


class ContributionCalendarMonth(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('first_day', 'name', 'total_weeks', 'year')
    first_day = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='firstDay')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    total_weeks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalWeeks')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class ContributionCalendarWeek(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('contribution_days', 'first_day')
    contribution_days = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContributionCalendarDay))), graphql_name='contributionDays')
    first_day = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='firstDay')


class ContributionsCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('commit_contributions_by_repository', 'contribution_calendar', 'contribution_years', 'does_end_in_current_month', 'earliest_restricted_contribution_date', 'ended_at', 'first_issue_contribution', 'first_pull_request_contribution', 'first_repository_contribution', 'has_activity_in_the_past', 'has_any_contributions', 'has_any_restricted_contributions', 'is_single_day', 'issue_contributions', 'issue_contributions_by_repository', 'joined_git_hub_contribution', 'latest_restricted_contribution_date', 'most_recent_collection_with_activity', 'most_recent_collection_without_activity', 'popular_issue_contribution', 'popular_pull_request_contribution', 'pull_request_contributions', 'pull_request_contributions_by_repository', 'pull_request_review_contributions', 'pull_request_review_contributions_by_repository', 'repository_contributions', 'restricted_contributions_count', 'started_at', 'total_commit_contributions', 'total_issue_contributions', 'total_pull_request_contributions', 'total_pull_request_review_contributions', 'total_repositories_with_contributed_commits', 'total_repositories_with_contributed_issues', 'total_repositories_with_contributed_pull_request_reviews', 'total_repositories_with_contributed_pull_requests', 'total_repository_contributions', 'user')
    commit_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommitContributionsByRepository))), graphql_name='commitContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
))
    )
    contribution_calendar = sgqlc.types.Field(sgqlc.types.non_null(ContributionCalendar), graphql_name='contributionCalendar')
    contribution_years = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='contributionYears')
    does_end_in_current_month = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doesEndInCurrentMonth')
    earliest_restricted_contribution_date = sgqlc.types.Field(Date, graphql_name='earliestRestrictedContributionDate')
    ended_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endedAt')
    first_issue_contribution = sgqlc.types.Field('CreatedIssueOrRestrictedContribution', graphql_name='firstIssueContribution')
    first_pull_request_contribution = sgqlc.types.Field('CreatedPullRequestOrRestrictedContribution', graphql_name='firstPullRequestContribution')
    first_repository_contribution = sgqlc.types.Field('CreatedRepositoryOrRestrictedContribution', graphql_name='firstRepositoryContribution')
    has_activity_in_the_past = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasActivityInThePast')
    has_any_contributions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAnyContributions')
    has_any_restricted_contributions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAnyRestrictedContributions')
    is_single_day = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSingleDay')
    issue_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedIssueContributionConnection'), graphql_name='issueContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    issue_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueContributionsByRepository'))), graphql_name='issueContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    joined_git_hub_contribution = sgqlc.types.Field('JoinedGitHubContribution', graphql_name='joinedGitHubContribution')
    latest_restricted_contribution_date = sgqlc.types.Field(Date, graphql_name='latestRestrictedContributionDate')
    most_recent_collection_with_activity = sgqlc.types.Field('ContributionsCollection', graphql_name='mostRecentCollectionWithActivity')
    most_recent_collection_without_activity = sgqlc.types.Field('ContributionsCollection', graphql_name='mostRecentCollectionWithoutActivity')
    popular_issue_contribution = sgqlc.types.Field('CreatedIssueContribution', graphql_name='popularIssueContribution')
    popular_pull_request_contribution = sgqlc.types.Field('CreatedPullRequestContribution', graphql_name='popularPullRequestContribution')
    pull_request_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedPullRequestContributionConnection'), graphql_name='pullRequestContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    pull_request_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PullRequestContributionsByRepository'))), graphql_name='pullRequestContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    pull_request_review_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedPullRequestReviewContributionConnection'), graphql_name='pullRequestReviewContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    pull_request_review_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PullRequestReviewContributionsByRepository'))), graphql_name='pullRequestReviewContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
))
    )
    repository_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedRepositoryContributionConnection'), graphql_name='repositoryContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    restricted_contributions_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='restrictedContributionsCount')
    started_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startedAt')
    total_commit_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCommitContributions')
    total_issue_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalIssueContributions', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_pull_request_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPullRequestContributions', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_pull_request_review_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPullRequestReviewContributions')
    total_repositories_with_contributed_commits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedCommits')
    total_repositories_with_contributed_issues = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedIssues', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_repositories_with_contributed_pull_request_reviews = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedPullRequestReviews')
    total_repositories_with_contributed_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedPullRequests', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_repository_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoryContributions', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class ConvertProjectCardNoteToIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_card')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card = sgqlc.types.Field('ProjectCard', graphql_name='projectCard')


class ConvertProjectV2DraftIssueItemToIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item = sgqlc.types.Field('ProjectV2Item', graphql_name='item')


class ConvertPullRequestToDraftPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class CopilotCodeReviewParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('review_draft_pull_requests', 'review_on_push')
    review_draft_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewDraftPullRequests')
    review_on_push = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewOnPush')


class CopilotEndpoints(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('api', 'origin_tracker', 'proxy', 'telemetry')
    api = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='api')
    origin_tracker = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='originTracker')
    proxy = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='proxy')
    telemetry = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='telemetry')


class CopyProjectV2Payload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class CreateAttributionInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner', 'source', 'target')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field('Organization', graphql_name='owner')
    source = sgqlc.types.Field('Claimable', graphql_name='source')
    target = sgqlc.types.Field('Claimable', graphql_name='target')


class CreateBranchProtectionRulePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('branch_protection_rule', 'client_mutation_id')
    branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='branchProtectionRule')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateCheckRunPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('check_run', 'client_mutation_id')
    check_run = sgqlc.types.Field('CheckRun', graphql_name='checkRun')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateCheckSuitePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('check_suite', 'client_mutation_id')
    check_suite = sgqlc.types.Field('CheckSuite', graphql_name='checkSuite')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateCommitOnBranchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'commit', 'ref')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    commit = sgqlc.types.Field('Commit', graphql_name='commit')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class CreateDeploymentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('auto_merged', 'client_mutation_id', 'deployment')
    auto_merged = sgqlc.types.Field(Boolean, graphql_name='autoMerged')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deployment = sgqlc.types.Field('Deployment', graphql_name='deployment')


class CreateDeploymentStatusPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deployment_status')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deployment_status = sgqlc.types.Field('DeploymentStatus', graphql_name='deploymentStatus')


class CreateDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class CreateEnterpriseOrganizationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class CreateEnvironmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment = sgqlc.types.Field('Environment', graphql_name='environment')


class CreateIpAllowListEntryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ip_allow_list_entry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ip_allow_list_entry = sgqlc.types.Field('IpAllowListEntry', graphql_name='ipAllowListEntry')


class CreateIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class CreateIssueTypePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_type = sgqlc.types.Field('IssueType', graphql_name='issueType')


class CreateLabelPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'label')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    label = sgqlc.types.Field('Label', graphql_name='label')


class CreateLinkedBranchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue', 'linked_branch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    linked_branch = sgqlc.types.Field('LinkedBranch', graphql_name='linkedBranch')


class CreateMigrationSourcePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'migration_source')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    migration_source = sgqlc.types.Field('MigrationSource', graphql_name='migrationSource')


class CreateProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class CreateProjectV2FieldPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2_field')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2_field = sgqlc.types.Field('ProjectV2FieldConfiguration', graphql_name='projectV2Field')


class CreateProjectV2Payload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class CreateProjectV2StatusUpdatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'status_update')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    status_update = sgqlc.types.Field('ProjectV2StatusUpdate', graphql_name='statusUpdate')


class CreatePullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class CreateRefPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ref')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class CreateRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class CreateRepositoryRulesetPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ruleset')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ruleset = sgqlc.types.Field('RepositoryRuleset', graphql_name='ruleset')


class CreateSponsorsListingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsors_listing')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsors_listing = sgqlc.types.Field('SponsorsListing', graphql_name='sponsorsListing')


class CreateSponsorsTierPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsors_tier')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsors_tier = sgqlc.types.Field('SponsorsTier', graphql_name='sponsorsTier')


class CreateSponsorshipPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsorship')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsorship = sgqlc.types.Field('Sponsorship', graphql_name='sponsorship')


class CreateSponsorshipsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsorables')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsorables = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Sponsorable)), graphql_name='sponsorables')


class CreateTeamDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateTeamDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateUserListPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'list', 'viewer')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    list = sgqlc.types.Field('UserList', graphql_name='list')
    viewer = sgqlc.types.Field('User', graphql_name='viewer')


class CreatedCommitContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedCommitContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedCommitContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedCommitContributionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedCommitContribution', graphql_name='node')


class CreatedIssueContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedIssueContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedIssueContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedIssueContributionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedIssueContribution', graphql_name='node')


class CreatedPullRequestContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedPullRequestContributionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedPullRequestContribution', graphql_name='node')


class CreatedPullRequestReviewContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestReviewContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestReviewContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedPullRequestReviewContributionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedPullRequestReviewContribution', graphql_name='node')


class CreatedRepositoryContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedRepositoryContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedRepositoryContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedRepositoryContributionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedRepositoryContribution', graphql_name='node')


class CvssSeverities(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cvss_v3', 'cvss_v4')
    cvss_v3 = sgqlc.types.Field(CVSS, graphql_name='cvssV3')
    cvss_v4 = sgqlc.types.Field(CVSS, graphql_name='cvssV4')


class DeclineTopicSuggestionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteBranchProtectionRulePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteDeploymentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('DiscussionComment', graphql_name='comment')


class DeleteDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class DeleteEnvironmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteIpAllowListEntryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ip_allow_list_entry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ip_allow_list_entry = sgqlc.types.Field('IpAllowListEntry', graphql_name='ipAllowListEntry')


class DeleteIssueCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class DeleteIssueTypePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_issue_type_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_issue_type_id = sgqlc.types.Field(ID, graphql_name='deletedIssueTypeId')


class DeleteLabelPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteLinkedBranchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class DeletePackageVersionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class DeleteProjectCardPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'column', 'deleted_card_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column = sgqlc.types.Field('ProjectColumn', graphql_name='column')
    deleted_card_id = sgqlc.types.Field(ID, graphql_name='deletedCardId')


class DeleteProjectColumnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_column_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_column_id = sgqlc.types.Field(ID, graphql_name='deletedColumnId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class DeleteProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field(ProjectOwner, graphql_name='owner')


class DeleteProjectV2FieldPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2_field')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2_field = sgqlc.types.Field('ProjectV2FieldConfiguration', graphql_name='projectV2Field')


class DeleteProjectV2ItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_item_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_item_id = sgqlc.types.Field(ID, graphql_name='deletedItemId')


class DeleteProjectV2Payload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class DeleteProjectV2StatusUpdatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_status_update_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_status_update_id = sgqlc.types.Field(ID, graphql_name='deletedStatusUpdateId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class DeleteProjectV2WorkflowPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_workflow_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_workflow_id = sgqlc.types.Field(ID, graphql_name='deletedWorkflowId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class DeletePullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review', 'pull_request_review_comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')
    pull_request_review_comment = sgqlc.types.Field('PullRequestReviewComment', graphql_name='pullRequestReviewComment')


class DeletePullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class DeleteRefPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteRepositoryRulesetPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteTeamDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteTeamDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteUserListPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class DeleteVerifiableDomainPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field('VerifiableDomainOwner', graphql_name='owner')


class DependabotUpdateError(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('body', 'error_type', 'title')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    error_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='errorType')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class DependencyGraphDependency(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_dependencies', 'package_manager', 'package_name', 'package_url', 'relationship', 'repository', 'requirements')
    has_dependencies = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDependencies')
    package_manager = sgqlc.types.Field(String, graphql_name='packageManager')
    package_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='packageName')
    package_url = sgqlc.types.Field(URI, graphql_name='packageUrl')
    relationship = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relationship')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    requirements = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requirements')


class DependencyGraphDependencyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DependencyGraphDependencyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(DependencyGraphDependency), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DependencyGraphDependencyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(DependencyGraphDependency, graphql_name='node')


class DependencyGraphManifestConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DependencyGraphManifestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DependencyGraphManifest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DependencyGraphManifestEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DependencyGraphManifest', graphql_name='node')


class DeployKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeployKeyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeployKey'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeployKeyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeployKey', graphql_name='node')


class DeploymentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Deployment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Deployment', graphql_name='node')


class DeploymentProtectionRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('database_id', 'prevent_self_review', 'reviewers', 'timeout', 'type')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    prevent_self_review = sgqlc.types.Field(Boolean, graphql_name='preventSelfReview')
    reviewers = sgqlc.types.Field(sgqlc.types.non_null('DeploymentReviewerConnection'), graphql_name='reviewers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    timeout = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timeout')
    type = sgqlc.types.Field(sgqlc.types.non_null(DeploymentProtectionRuleType), graphql_name='type')


class DeploymentProtectionRuleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentProtectionRuleEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(DeploymentProtectionRule), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentProtectionRuleEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(DeploymentProtectionRule, graphql_name='node')


class DeploymentRequest(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('current_user_can_approve', 'environment', 'reviewers', 'wait_timer', 'wait_timer_started_at')
    current_user_can_approve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='currentUserCanApprove')
    environment = sgqlc.types.Field(sgqlc.types.non_null('Environment'), graphql_name='environment')
    reviewers = sgqlc.types.Field(sgqlc.types.non_null('DeploymentReviewerConnection'), graphql_name='reviewers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    wait_timer = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='waitTimer')
    wait_timer_started_at = sgqlc.types.Field(DateTime, graphql_name='waitTimerStartedAt')


class DeploymentRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(DeploymentRequest), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentRequestEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(DeploymentRequest, graphql_name='node')


class DeploymentReviewConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentReviewEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeploymentReview'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentReviewEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeploymentReview', graphql_name='node')


class DeploymentReviewerConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentReviewerEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeploymentReviewer'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentReviewerEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeploymentReviewer', graphql_name='node')


class DeploymentStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentStatusEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeploymentStatus'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentStatusEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeploymentStatus', graphql_name='node')


class DequeuePullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'merge_queue_entry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    merge_queue_entry = sgqlc.types.Field('MergeQueueEntry', graphql_name='mergeQueueEntry')


class DisablePullRequestAutoMergePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class DiscussionCategoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DiscussionCategoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DiscussionCategory'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DiscussionCategoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DiscussionCategory', graphql_name='node')


class DiscussionCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DiscussionCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DiscussionComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DiscussionCommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DiscussionComment', graphql_name='node')


class DiscussionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DiscussionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Discussion'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DiscussionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Discussion', graphql_name='node')


class DiscussionPollOptionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('DiscussionPollOptionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DiscussionPollOption'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DiscussionPollOptionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DiscussionPollOption', graphql_name='node')


class DismissPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class DismissRepositoryVulnerabilityAlertPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_vulnerability_alert')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_vulnerability_alert = sgqlc.types.Field('RepositoryVulnerabilityAlert', graphql_name='repositoryVulnerabilityAlert')


class EPSS(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('percentage', 'percentile')
    percentage = sgqlc.types.Field(Float, graphql_name='percentage')
    percentile = sgqlc.types.Field(Float, graphql_name='percentile')


class EnablePullRequestAutoMergePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class EnqueuePullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'merge_queue_entry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    merge_queue_entry = sgqlc.types.Field('MergeQueueEntry', graphql_name='mergeQueueEntry')


class EnterpriseAdministratorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseAdministratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseAdministratorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'role')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role')


class EnterpriseAdministratorInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseAdministratorInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseAdministratorInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseAdministratorInvitationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='node')


class EnterpriseBillingInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_licensable_users_count', 'asset_packs', 'bandwidth_quota', 'bandwidth_usage', 'bandwidth_usage_percentage', 'storage_quota', 'storage_usage', 'storage_usage_percentage', 'total_available_licenses', 'total_licenses')
    all_licensable_users_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='allLicensableUsersCount')
    asset_packs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetPacks')
    bandwidth_quota = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='bandwidthQuota')
    bandwidth_usage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='bandwidthUsage')
    bandwidth_usage_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bandwidthUsagePercentage')
    storage_quota = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='storageQuota')
    storage_usage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='storageUsage')
    storage_usage_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='storageUsagePercentage')
    total_available_licenses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalAvailableLicenses')
    total_licenses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalLicenses')


class EnterpriseConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Enterprise'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Enterprise', graphql_name='node')


class EnterpriseFailedInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count', 'total_unique_user_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseFailedInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_unique_user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalUniqueUserCount')


class EnterpriseFailedInvitationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationInvitation', graphql_name='node')


class EnterpriseMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseMember'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseMemberEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseMember', graphql_name='node')


class EnterpriseMemberInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseMemberInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseMemberInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseMemberInvitationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseMemberInvitation', graphql_name='node')


class EnterpriseOrganizationMembershipConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseOrganizationMembershipEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseOrganizationMembershipEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'role')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseUserAccountMembershipRole), graphql_name='role')


class EnterpriseOutsideCollaboratorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseOutsideCollaboratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseOutsideCollaboratorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'repositories')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    repositories = sgqlc.types.Field(sgqlc.types.non_null('EnterpriseRepositoryInfoConnection'), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
))
    )


class EnterpriseOwnerInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('admins', 'affiliated_users_with_two_factor_disabled', 'affiliated_users_with_two_factor_disabled_exist', 'allow_private_repository_forking_setting', 'allow_private_repository_forking_setting_organizations', 'allow_private_repository_forking_setting_policy_value', 'default_repository_permission_setting', 'default_repository_permission_setting_organizations', 'domains', 'enterprise_server_installations', 'failed_invitations', 'ip_allow_list_enabled_setting', 'ip_allow_list_entries', 'ip_allow_list_for_installed_apps_enabled_setting', 'is_updating_default_repository_permission', 'is_updating_two_factor_requirement', 'members_can_change_repository_visibility_setting', 'members_can_change_repository_visibility_setting_organizations', 'members_can_create_internal_repositories_setting', 'members_can_create_private_repositories_setting', 'members_can_create_public_repositories_setting', 'members_can_create_repositories_setting', 'members_can_create_repositories_setting_organizations', 'members_can_delete_issues_setting', 'members_can_delete_issues_setting_organizations', 'members_can_delete_repositories_setting', 'members_can_delete_repositories_setting_organizations', 'members_can_invite_collaborators_setting', 'members_can_invite_collaborators_setting_organizations', 'members_can_make_purchases_setting', 'members_can_update_protected_branches_setting', 'members_can_update_protected_branches_setting_organizations', 'members_can_view_dependency_insights_setting', 'members_can_view_dependency_insights_setting_organizations', 'notification_delivery_restriction_enabled_setting', 'oidc_provider', 'organization_projects_setting', 'organization_projects_setting_organizations', 'outside_collaborators', 'pending_admin_invitations', 'pending_collaborator_invitations', 'pending_member_invitations', 'pending_unaffiliated_member_invitations', 'repository_deploy_key_setting', 'repository_deploy_key_setting_organizations', 'repository_projects_setting', 'repository_projects_setting_organizations', 'saml_identity_provider', 'saml_identity_provider_setting_organizations', 'support_entitlements', 'team_discussions_setting', 'team_discussions_setting_organizations', 'two_factor_disallowed_methods_setting', 'two_factor_required_setting', 'two_factor_required_setting_organizations')
    admins = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorConnection), graphql_name='admins', args=sgqlc.types.ArgDict((
        ('organization_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='organizationLogins', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('role', sgqlc.types.Arg(EnterpriseAdministratorRole, graphql_name='role', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('has_two_factor_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasTwoFactorEnabled', default=None)),
        ('two_factor_method_security', sgqlc.types.Arg(TwoFactorCredentialSecurityType, graphql_name='twoFactorMethodSecurity', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    affiliated_users_with_two_factor_disabled = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='affiliatedUsersWithTwoFactorDisabled', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    affiliated_users_with_two_factor_disabled_exist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='affiliatedUsersWithTwoFactorDisabledExist')
    allow_private_repository_forking_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='allowPrivateRepositoryForkingSetting')
    allow_private_repository_forking_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='allowPrivateRepositoryForkingSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    allow_private_repository_forking_setting_policy_value = sgqlc.types.Field(EnterpriseAllowPrivateRepositoryForkingPolicyValue, graphql_name='allowPrivateRepositoryForkingSettingPolicyValue')
    default_repository_permission_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseDefaultRepositoryPermissionSettingValue), graphql_name='defaultRepositoryPermissionSetting')
    default_repository_permission_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='defaultRepositoryPermissionSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(DefaultRepositoryPermissionField), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    domains = sgqlc.types.Field(sgqlc.types.non_null('VerifiableDomainConnection'), graphql_name='domains', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_verified', sgqlc.types.Arg(Boolean, graphql_name='isVerified', default=None)),
        ('is_approved', sgqlc.types.Arg(Boolean, graphql_name='isApproved', default=None)),
        ('order_by', sgqlc.types.Arg(VerifiableDomainOrder, graphql_name='orderBy', default={'field': 'DOMAIN', 'direction': 'ASC'})),
))
    )
    enterprise_server_installations = sgqlc.types.Field(sgqlc.types.non_null('EnterpriseServerInstallationConnection'), graphql_name='enterpriseServerInstallations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('connected_only', sgqlc.types.Arg(Boolean, graphql_name='connectedOnly', default=False)),
        ('order_by', sgqlc.types.Arg(EnterpriseServerInstallationOrder, graphql_name='orderBy', default={'field': 'HOST_NAME', 'direction': 'ASC'})),
))
    )
    failed_invitations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseFailedInvitationConnection), graphql_name='failedInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    ip_allow_list_enabled_setting = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListEnabledSettingValue), graphql_name='ipAllowListEnabledSetting')
    ip_allow_list_entries = sgqlc.types.Field(sgqlc.types.non_null('IpAllowListEntryConnection'), graphql_name='ipAllowListEntries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(IpAllowListEntryOrder, graphql_name='orderBy', default={'field': 'ALLOW_LIST_VALUE', 'direction': 'ASC'})),
))
    )
    ip_allow_list_for_installed_apps_enabled_setting = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListForInstalledAppsEnabledSettingValue), graphql_name='ipAllowListForInstalledAppsEnabledSetting')
    is_updating_default_repository_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUpdatingDefaultRepositoryPermission')
    is_updating_two_factor_requirement = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUpdatingTwoFactorRequirement')
    members_can_change_repository_visibility_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanChangeRepositoryVisibilitySetting')
    members_can_change_repository_visibility_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanChangeRepositoryVisibilitySettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_create_internal_repositories_setting = sgqlc.types.Field(Boolean, graphql_name='membersCanCreateInternalRepositoriesSetting')
    members_can_create_private_repositories_setting = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePrivateRepositoriesSetting')
    members_can_create_public_repositories_setting = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePublicRepositoriesSetting')
    members_can_create_repositories_setting = sgqlc.types.Field(EnterpriseMembersCanCreateRepositoriesSettingValue, graphql_name='membersCanCreateRepositoriesSetting')
    members_can_create_repositories_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanCreateRepositoriesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationMembersCanCreateRepositoriesSettingValue), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_delete_issues_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanDeleteIssuesSetting')
    members_can_delete_issues_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanDeleteIssuesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_delete_repositories_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanDeleteRepositoriesSetting')
    members_can_delete_repositories_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanDeleteRepositoriesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_invite_collaborators_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanInviteCollaboratorsSetting')
    members_can_invite_collaborators_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanInviteCollaboratorsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_make_purchases_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMembersCanMakePurchasesSettingValue), graphql_name='membersCanMakePurchasesSetting')
    members_can_update_protected_branches_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanUpdateProtectedBranchesSetting')
    members_can_update_protected_branches_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanUpdateProtectedBranchesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_view_dependency_insights_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanViewDependencyInsightsSetting')
    members_can_view_dependency_insights_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanViewDependencyInsightsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    notification_delivery_restriction_enabled_setting = sgqlc.types.Field(sgqlc.types.non_null(NotificationRestrictionSettingValue), graphql_name='notificationDeliveryRestrictionEnabledSetting')
    oidc_provider = sgqlc.types.Field('OIDCProvider', graphql_name='oidcProvider')
    organization_projects_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='organizationProjectsSetting')
    organization_projects_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='organizationProjectsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    outside_collaborators = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseOutsideCollaboratorConnection), graphql_name='outsideCollaborators', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('visibility', sgqlc.types.Arg(RepositoryVisibility, graphql_name='visibility', default=None)),
        ('has_two_factor_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasTwoFactorEnabled', default=None)),
        ('two_factor_method_security', sgqlc.types.Arg(TwoFactorCredentialSecurityType, graphql_name='twoFactorMethodSecurity', default=None)),
        ('organization_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='organizationLogins', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_admin_invitations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorInvitationConnection), graphql_name='pendingAdminInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseAdministratorInvitationOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('role', sgqlc.types.Arg(EnterpriseAdministratorRole, graphql_name='role', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_collaborator_invitations = sgqlc.types.Field(sgqlc.types.non_null('RepositoryInvitationConnection'), graphql_name='pendingCollaboratorInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryInvitationOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_member_invitations = sgqlc.types.Field(sgqlc.types.non_null('EnterprisePendingMemberInvitationConnection'), graphql_name='pendingMemberInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('organization_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='organizationLogins', default=None)),
        ('invitation_source', sgqlc.types.Arg(OrganizationInvitationSource, graphql_name='invitationSource', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_unaffiliated_member_invitations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberInvitationConnection), graphql_name='pendingUnaffiliatedMemberInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberInvitationOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository_deploy_key_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='repositoryDeployKeySetting')
    repository_deploy_key_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='repositoryDeployKeySettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    repository_projects_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='repositoryProjectsSetting')
    repository_projects_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='repositoryProjectsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    saml_identity_provider = sgqlc.types.Field('EnterpriseIdentityProvider', graphql_name='samlIdentityProvider')
    saml_identity_provider_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='samlIdentityProviderSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(IdentityProviderConfigurationState), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    support_entitlements = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberConnection), graphql_name='supportEntitlements', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    team_discussions_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='teamDiscussionsSetting')
    team_discussions_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='teamDiscussionsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    two_factor_disallowed_methods_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseDisallowedMethodsSettingValue), graphql_name='twoFactorDisallowedMethodsSetting')
    two_factor_required_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledSettingValue), graphql_name='twoFactorRequiredSetting')
    two_factor_required_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='twoFactorRequiredSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )


class EnterprisePendingMemberInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count', 'total_unique_user_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterprisePendingMemberInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_unique_user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalUniqueUserCount')


class EnterprisePendingMemberInvitationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationInvitation', graphql_name='node')


class EnterpriseRepositoryInfoConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseRepositoryInfoEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseRepositoryInfo'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseRepositoryInfoEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseRepositoryInfo', graphql_name='node')


class EnterpriseServerInstallationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerInstallationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerInstallation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerInstallationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerInstallation', graphql_name='node')


class EnterpriseServerInstallationMembershipConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerInstallationMembershipEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerInstallation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerInstallationMembershipEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'role')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerInstallation', graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseUserAccountMembershipRole), graphql_name='role')


class EnterpriseServerUserAccountConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccount'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerUserAccountEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerUserAccount', graphql_name='node')


class EnterpriseServerUserAccountEmailConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountEmailEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountEmail'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerUserAccountEmailEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerUserAccountEmail', graphql_name='node')


class EnterpriseServerUserAccountsUploadConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountsUploadEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountsUpload'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerUserAccountsUploadEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerUserAccountsUpload', graphql_name='node')


class EnvironmentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnvironmentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Environment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnvironmentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Environment', graphql_name='node')


class ExternalIdentityAttribute(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metadata', 'name', 'value')
    metadata = sgqlc.types.Field(String, graphql_name='metadata')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class ExternalIdentityConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ExternalIdentityEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ExternalIdentity'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ExternalIdentityEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ExternalIdentity', graphql_name='node')


class ExternalIdentitySamlAttributes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('attributes', 'emails', 'family_name', 'given_name', 'groups', 'name_id', 'username')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ExternalIdentityAttribute))), graphql_name='attributes')
    emails = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserEmailMetadata')), graphql_name='emails')
    family_name = sgqlc.types.Field(String, graphql_name='familyName')
    given_name = sgqlc.types.Field(String, graphql_name='givenName')
    groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='groups')
    name_id = sgqlc.types.Field(String, graphql_name='nameId')
    username = sgqlc.types.Field(String, graphql_name='username')


class ExternalIdentityScimAttributes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('emails', 'family_name', 'given_name', 'groups', 'username')
    emails = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserEmailMetadata')), graphql_name='emails')
    family_name = sgqlc.types.Field(String, graphql_name='familyName')
    given_name = sgqlc.types.Field(String, graphql_name='givenName')
    groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='groups')
    username = sgqlc.types.Field(String, graphql_name='username')


class FileExtensionRestrictionParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('restricted_file_extensions',)
    restricted_file_extensions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='restrictedFileExtensions')


class FilePathRestrictionParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('restricted_file_paths',)
    restricted_file_paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='restrictedFilePaths')


class FollowOrganizationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class FollowUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class FollowerConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FollowingConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FundingLink(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('platform', 'url')
    platform = sgqlc.types.Field(sgqlc.types.non_null(FundingPlatform), graphql_name='platform')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class GistCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('GistCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('GistComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GistCommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('GistComment', graphql_name='node')


class GistConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('GistEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Gist'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GistEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Gist', graphql_name='node')


class GistFile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('encoded_name', 'encoding', 'extension', 'is_image', 'is_truncated', 'language', 'name', 'size', 'text')
    encoded_name = sgqlc.types.Field(String, graphql_name='encodedName')
    encoding = sgqlc.types.Field(String, graphql_name='encoding')
    extension = sgqlc.types.Field(String, graphql_name='extension')
    is_image = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImage')
    is_truncated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTruncated')
    language = sgqlc.types.Field('Language', graphql_name='language')
    name = sgqlc.types.Field(String, graphql_name='name')
    size = sgqlc.types.Field(Int, graphql_name='size')
    text = sgqlc.types.Field(String, graphql_name='text', args=sgqlc.types.ArgDict((
        ('truncate', sgqlc.types.Arg(Int, graphql_name='truncate', default=None)),
))
    )


class GitActor(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('avatar_url', 'date', 'email', 'name', 'user')
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    date = sgqlc.types.Field(GitTimestamp, graphql_name='date')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    user = sgqlc.types.Field('User', graphql_name='user')


class GitActorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('GitActorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(GitActor), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GitActorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(GitActor, graphql_name='node')


class GitHubMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('git_hub_services_sha', 'git_ip_addresses', 'github_enterprise_importer_ip_addresses', 'hook_ip_addresses', 'importer_ip_addresses', 'is_password_authentication_verifiable', 'pages_ip_addresses')
    git_hub_services_sha = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='gitHubServicesSha')
    git_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gitIpAddresses')
    github_enterprise_importer_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='githubEnterpriseImporterIpAddresses')
    hook_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hookIpAddresses')
    importer_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='importerIpAddresses')
    is_password_authentication_verifiable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPasswordAuthenticationVerifiable')
    pages_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pagesIpAddresses')


class GrantEnterpriseOrganizationsMigratorRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organizations')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organizations = sgqlc.types.Field('OrganizationConnection', graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class GrantMigratorRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class Hovercard(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('contexts',)
    contexts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HovercardContext))), graphql_name='contexts')


class ImportProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class InviteEnterpriseAdminPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='invitation')


class InviteEnterpriseMemberPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseMemberInvitation', graphql_name='invitation')


class IpAllowListEntryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IpAllowListEntryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IpAllowListEntry'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IpAllowListEntryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IpAllowListEntry', graphql_name='node')


class IssueCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueCommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueComment', graphql_name='node')


class IssueConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Issue'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueContributionsByRepository(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('contributions', 'repository')
    contributions = sgqlc.types.Field(sgqlc.types.non_null(CreatedIssueContributionConnection), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class IssueDependenciesSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('blocked_by', 'blocking', 'total_blocked_by', 'total_blocking')
    blocked_by = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blockedBy')
    blocking = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blocking')
    total_blocked_by = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalBlockedBy')
    total_blocking = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalBlocking')


class IssueEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Issue', graphql_name='node')


class IssueTemplate(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('about', 'assignees', 'body', 'filename', 'labels', 'name', 'title', 'type')
    about = sgqlc.types.Field(String, graphql_name='about')
    assignees = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    body = sgqlc.types.Field(String, graphql_name='body')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    labels = sgqlc.types.Field('LabelConnection', graphql_name='labels', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(LabelOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field('IssueType', graphql_name='type')


class IssueTimelineConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueTimelineItemEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueTimelineItem', graphql_name='node')


class IssueTimelineItemsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'filtered_count', 'nodes', 'page_count', 'page_info', 'total_count', 'updated_at')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItemsEdge'), graphql_name='edges')
    filtered_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filteredCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItems'), graphql_name='nodes')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class IssueTimelineItemsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueTimelineItems', graphql_name='node')


class IssueTypeConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueTypeEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueType'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueTypeEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueType', graphql_name='node')


class LabelConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('LabelEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Label'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LabelEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Label', graphql_name='node')


class LanguageConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count', 'total_size')
    edges = sgqlc.types.Field(sgqlc.types.list_of('LanguageEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Language'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalSize')


class LanguageEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'size')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Language'), graphql_name='node')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')


class LicenseRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('description', 'key', 'label')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class LinkProjectV2ToRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class LinkProjectV2ToTeamPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'team')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team = sgqlc.types.Field('Team', graphql_name='team')


class LinkRepositoryToProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class LinkedBranchConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('LinkedBranchEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('LinkedBranch'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LinkedBranchEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('LinkedBranch', graphql_name='node')


class LockLockablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'locked_record')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    locked_record = sgqlc.types.Field(Lockable, graphql_name='lockedRecord')


class MannequinConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('MannequinEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Mannequin'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MannequinEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Mannequin', graphql_name='node')


class MarkDiscussionCommentAsAnswerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class MarkFileAsViewedPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class MarkProjectV2AsTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class MarkPullRequestReadyForReviewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class MarketplaceListingConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('MarketplaceListingEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('MarketplaceListing'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketplaceListingEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('MarketplaceListing', graphql_name='node')


class MaxFilePathLengthParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('max_file_path_length',)
    max_file_path_length = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxFilePathLength')


class MaxFileSizeParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('max_file_size',)
    max_file_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxFileSize')


class MergeBranchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'merge_commit')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    merge_commit = sgqlc.types.Field('Commit', graphql_name='mergeCommit')


class MergePullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class MergeQueueConfiguration(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('check_response_timeout', 'maximum_entries_to_build', 'maximum_entries_to_merge', 'merge_method', 'merging_strategy', 'minimum_entries_to_merge', 'minimum_entries_to_merge_wait_time')
    check_response_timeout = sgqlc.types.Field(Int, graphql_name='checkResponseTimeout')
    maximum_entries_to_build = sgqlc.types.Field(Int, graphql_name='maximumEntriesToBuild')
    maximum_entries_to_merge = sgqlc.types.Field(Int, graphql_name='maximumEntriesToMerge')
    merge_method = sgqlc.types.Field(PullRequestMergeMethod, graphql_name='mergeMethod')
    merging_strategy = sgqlc.types.Field(MergeQueueMergingStrategy, graphql_name='mergingStrategy')
    minimum_entries_to_merge = sgqlc.types.Field(Int, graphql_name='minimumEntriesToMerge')
    minimum_entries_to_merge_wait_time = sgqlc.types.Field(Int, graphql_name='minimumEntriesToMergeWaitTime')


class MergeQueueEntryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('MergeQueueEntryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('MergeQueueEntry'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MergeQueueEntryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('MergeQueueEntry', graphql_name='node')


class MergeQueueParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('check_response_timeout_minutes', 'grouping_strategy', 'max_entries_to_build', 'max_entries_to_merge', 'merge_method', 'min_entries_to_merge', 'min_entries_to_merge_wait_minutes')
    check_response_timeout_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='checkResponseTimeoutMinutes')
    grouping_strategy = sgqlc.types.Field(sgqlc.types.non_null(MergeQueueGroupingStrategy), graphql_name='groupingStrategy')
    max_entries_to_build = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxEntriesToBuild')
    max_entries_to_merge = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxEntriesToMerge')
    merge_method = sgqlc.types.Field(sgqlc.types.non_null(MergeQueueMergeMethod), graphql_name='mergeMethod')
    min_entries_to_merge = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minEntriesToMerge')
    min_entries_to_merge_wait_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minEntriesToMergeWaitMinutes')


class MilestoneConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('MilestoneEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Milestone'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MilestoneEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Milestone', graphql_name='node')


class MinimizeCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'minimized_comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    minimized_comment = sgqlc.types.Field(Minimizable, graphql_name='minimizedComment')


class MoveProjectCardPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('card_edge', 'client_mutation_id')
    card_edge = sgqlc.types.Field('ProjectCardEdge', graphql_name='cardEdge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MoveProjectColumnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'column_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_edge = sgqlc.types.Field('ProjectColumnEdge', graphql_name='columnEdge')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('abort_queued_migrations', 'abort_repository_migration', 'accept_enterprise_administrator_invitation', 'accept_enterprise_member_invitation', 'accept_topic_suggestion', 'access_user_namespace_repository', 'add_assignees_to_assignable', 'add_blocked_by', 'add_comment', 'add_discussion_comment', 'add_discussion_poll_vote', 'add_enterprise_organization_member', 'add_enterprise_support_entitlement', 'add_labels_to_labelable', 'add_project_v2_draft_issue', 'add_project_v2_item_by_id', 'add_pull_request_review', 'add_pull_request_review_comment', 'add_pull_request_review_thread', 'add_pull_request_review_thread_reply', 'add_reaction', 'add_star', 'add_sub_issue', 'add_upvote', 'add_verifiable_domain', 'approve_deployments', 'approve_verifiable_domain', 'archive_project_v2_item', 'archive_repository', 'cancel_enterprise_admin_invitation', 'cancel_enterprise_member_invitation', 'cancel_sponsorship', 'change_user_status', 'clear_labels_from_labelable', 'clear_project_v2_item_field_value', 'clone_template_repository', 'close_discussion', 'close_issue', 'close_pull_request', 'convert_project_v2_draft_issue_item_to_issue', 'convert_pull_request_to_draft', 'copy_project_v2', 'create_attribution_invitation', 'create_branch_protection_rule', 'create_check_run', 'create_check_suite', 'create_commit_on_branch', 'create_deployment', 'create_deployment_status', 'create_discussion', 'create_enterprise_organization', 'create_environment', 'create_ip_allow_list_entry', 'create_issue', 'create_issue_type', 'create_label', 'create_linked_branch', 'create_migration_source', 'create_project_v2', 'create_project_v2_field', 'create_project_v2_status_update', 'create_pull_request', 'create_ref', 'create_repository', 'create_repository_ruleset', 'create_sponsors_listing', 'create_sponsors_tier', 'create_sponsorship', 'create_sponsorships', 'create_team_discussion', 'create_team_discussion_comment', 'create_user_list', 'decline_topic_suggestion', 'delete_branch_protection_rule', 'delete_deployment', 'delete_discussion', 'delete_discussion_comment', 'delete_environment', 'delete_ip_allow_list_entry', 'delete_issue', 'delete_issue_comment', 'delete_issue_type', 'delete_label', 'delete_linked_branch', 'delete_package_version', 'delete_project_v2', 'delete_project_v2_field', 'delete_project_v2_item', 'delete_project_v2_status_update', 'delete_project_v2_workflow', 'delete_pull_request_review', 'delete_pull_request_review_comment', 'delete_ref', 'delete_repository_ruleset', 'delete_team_discussion', 'delete_team_discussion_comment', 'delete_user_list', 'delete_verifiable_domain', 'dequeue_pull_request', 'disable_pull_request_auto_merge', 'dismiss_pull_request_review', 'dismiss_repository_vulnerability_alert', 'enable_pull_request_auto_merge', 'enqueue_pull_request', 'follow_organization', 'follow_user', 'grant_enterprise_organizations_migrator_role', 'grant_migrator_role', 'invite_enterprise_admin', 'invite_enterprise_member', 'link_project_v2_to_repository', 'link_project_v2_to_team', 'lock_lockable', 'mark_discussion_comment_as_answer', 'mark_file_as_viewed', 'mark_project_v2_as_template', 'mark_pull_request_ready_for_review', 'merge_branch', 'merge_pull_request', 'minimize_comment', 'pin_environment', 'pin_issue', 'publish_sponsors_tier', 'regenerate_enterprise_identity_provider_recovery_codes', 'regenerate_verifiable_domain_token', 'reject_deployments', 'remove_assignees_from_assignable', 'remove_blocked_by', 'remove_enterprise_admin', 'remove_enterprise_identity_provider', 'remove_enterprise_member', 'remove_enterprise_organization', 'remove_enterprise_support_entitlement', 'remove_labels_from_labelable', 'remove_outside_collaborator', 'remove_reaction', 'remove_star', 'remove_sub_issue', 'remove_upvote', 'reopen_discussion', 'reopen_issue', 'reopen_pull_request', 'reorder_environment', 'replace_actors_for_assignable', 'reprioritize_sub_issue', 'request_reviews', 'rerequest_check_suite', 'resolve_review_thread', 'retire_sponsors_tier', 'revert_pull_request', 'revoke_enterprise_organizations_migrator_role', 'revoke_migrator_role', 'set_enterprise_identity_provider', 'set_organization_interaction_limit', 'set_repository_interaction_limit', 'set_user_interaction_limit', 'start_organization_migration', 'start_repository_migration', 'submit_pull_request_review', 'transfer_enterprise_organization', 'transfer_issue', 'unarchive_project_v2_item', 'unarchive_repository', 'unfollow_organization', 'unfollow_user', 'unlink_project_v2_from_repository', 'unlink_project_v2_from_team', 'unlock_lockable', 'unmark_discussion_comment_as_answer', 'unmark_file_as_viewed', 'unmark_issue_as_duplicate', 'unmark_project_v2_as_template', 'unminimize_comment', 'unpin_issue', 'unresolve_review_thread', 'update_branch_protection_rule', 'update_check_run', 'update_check_suite_preferences', 'update_discussion', 'update_discussion_comment', 'update_enterprise_administrator_role', 'update_enterprise_allow_private_repository_forking_setting', 'update_enterprise_default_repository_permission_setting', 'update_enterprise_deploy_key_setting', 'update_enterprise_members_can_change_repository_visibility_setting', 'update_enterprise_members_can_create_repositories_setting', 'update_enterprise_members_can_delete_issues_setting', 'update_enterprise_members_can_delete_repositories_setting', 'update_enterprise_members_can_invite_collaborators_setting', 'update_enterprise_members_can_make_purchases_setting', 'update_enterprise_members_can_update_protected_branches_setting', 'update_enterprise_members_can_view_dependency_insights_setting', 'update_enterprise_organization_projects_setting', 'update_enterprise_owner_organization_role', 'update_enterprise_profile', 'update_enterprise_repository_projects_setting', 'update_enterprise_team_discussions_setting', 'update_enterprise_two_factor_authentication_disallowed_methods_setting', 'update_enterprise_two_factor_authentication_required_setting', 'update_environment', 'update_ip_allow_list_enabled_setting', 'update_ip_allow_list_entry', 'update_ip_allow_list_for_installed_apps_enabled_setting', 'update_issue', 'update_issue_comment', 'update_issue_issue_type', 'update_issue_type', 'update_label', 'update_notification_restriction_setting', 'update_organization_allow_private_repository_forking_setting', 'update_organization_web_commit_signoff_setting', 'update_patreon_sponsorability', 'update_project_v2', 'update_project_v2_collaborators', 'update_project_v2_draft_issue', 'update_project_v2_field', 'update_project_v2_item_field_value', 'update_project_v2_item_position', 'update_project_v2_status_update', 'update_pull_request', 'update_pull_request_branch', 'update_pull_request_review', 'update_pull_request_review_comment', 'update_ref', 'update_refs', 'update_repository', 'update_repository_ruleset', 'update_repository_web_commit_signoff_setting', 'update_sponsorship_preferences', 'update_subscription', 'update_team_discussion', 'update_team_discussion_comment', 'update_team_review_assignment', 'update_teams_repository', 'update_topics', 'update_user_list', 'update_user_lists_for_item', 'verify_verifiable_domain')
    abort_queued_migrations = sgqlc.types.Field(AbortQueuedMigrationsPayload, graphql_name='abortQueuedMigrations', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AbortQueuedMigrationsInput), graphql_name='input', default=None)),
))
    )
    abort_repository_migration = sgqlc.types.Field(AbortRepositoryMigrationPayload, graphql_name='abortRepositoryMigration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AbortRepositoryMigrationInput), graphql_name='input', default=None)),
))
    )
    accept_enterprise_administrator_invitation = sgqlc.types.Field(AcceptEnterpriseAdministratorInvitationPayload, graphql_name='acceptEnterpriseAdministratorInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptEnterpriseAdministratorInvitationInput), graphql_name='input', default=None)),
))
    )
    accept_enterprise_member_invitation = sgqlc.types.Field(AcceptEnterpriseMemberInvitationPayload, graphql_name='acceptEnterpriseMemberInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptEnterpriseMemberInvitationInput), graphql_name='input', default=None)),
))
    )
    accept_topic_suggestion = sgqlc.types.Field(AcceptTopicSuggestionPayload, graphql_name='acceptTopicSuggestion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptTopicSuggestionInput), graphql_name='input', default=None)),
))
    )
    access_user_namespace_repository = sgqlc.types.Field(AccessUserNamespaceRepositoryPayload, graphql_name='accessUserNamespaceRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AccessUserNamespaceRepositoryInput), graphql_name='input', default=None)),
))
    )
    add_assignees_to_assignable = sgqlc.types.Field(AddAssigneesToAssignablePayload, graphql_name='addAssigneesToAssignable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddAssigneesToAssignableInput), graphql_name='input', default=None)),
))
    )
    add_blocked_by = sgqlc.types.Field(AddBlockedByPayload, graphql_name='addBlockedBy', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddBlockedByInput), graphql_name='input', default=None)),
))
    )
    add_comment = sgqlc.types.Field(AddCommentPayload, graphql_name='addComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddCommentInput), graphql_name='input', default=None)),
))
    )
    add_discussion_comment = sgqlc.types.Field(AddDiscussionCommentPayload, graphql_name='addDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    add_discussion_poll_vote = sgqlc.types.Field(AddDiscussionPollVotePayload, graphql_name='addDiscussionPollVote', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddDiscussionPollVoteInput), graphql_name='input', default=None)),
))
    )
    add_enterprise_organization_member = sgqlc.types.Field(AddEnterpriseOrganizationMemberPayload, graphql_name='addEnterpriseOrganizationMember', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddEnterpriseOrganizationMemberInput), graphql_name='input', default=None)),
))
    )
    add_enterprise_support_entitlement = sgqlc.types.Field(AddEnterpriseSupportEntitlementPayload, graphql_name='addEnterpriseSupportEntitlement', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddEnterpriseSupportEntitlementInput), graphql_name='input', default=None)),
))
    )
    add_labels_to_labelable = sgqlc.types.Field(AddLabelsToLabelablePayload, graphql_name='addLabelsToLabelable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddLabelsToLabelableInput), graphql_name='input', default=None)),
))
    )
    add_project_v2_draft_issue = sgqlc.types.Field(AddProjectV2DraftIssuePayload, graphql_name='addProjectV2DraftIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectV2DraftIssueInput), graphql_name='input', default=None)),
))
    )
    add_project_v2_item_by_id = sgqlc.types.Field(AddProjectV2ItemByIdPayload, graphql_name='addProjectV2ItemById', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectV2ItemByIdInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review = sgqlc.types.Field(AddPullRequestReviewPayload, graphql_name='addPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review_comment = sgqlc.types.Field(AddPullRequestReviewCommentPayload, graphql_name='addPullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review_thread = sgqlc.types.Field(AddPullRequestReviewThreadPayload, graphql_name='addPullRequestReviewThread', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewThreadInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review_thread_reply = sgqlc.types.Field(AddPullRequestReviewThreadReplyPayload, graphql_name='addPullRequestReviewThreadReply', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewThreadReplyInput), graphql_name='input', default=None)),
))
    )
    add_reaction = sgqlc.types.Field(AddReactionPayload, graphql_name='addReaction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddReactionInput), graphql_name='input', default=None)),
))
    )
    add_star = sgqlc.types.Field(AddStarPayload, graphql_name='addStar', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddStarInput), graphql_name='input', default=None)),
))
    )
    add_sub_issue = sgqlc.types.Field(AddSubIssuePayload, graphql_name='addSubIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddSubIssueInput), graphql_name='input', default=None)),
))
    )
    add_upvote = sgqlc.types.Field(AddUpvotePayload, graphql_name='addUpvote', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddUpvoteInput), graphql_name='input', default=None)),
))
    )
    add_verifiable_domain = sgqlc.types.Field(AddVerifiableDomainPayload, graphql_name='addVerifiableDomain', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddVerifiableDomainInput), graphql_name='input', default=None)),
))
    )
    approve_deployments = sgqlc.types.Field(ApproveDeploymentsPayload, graphql_name='approveDeployments', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveDeploymentsInput), graphql_name='input', default=None)),
))
    )
    approve_verifiable_domain = sgqlc.types.Field(ApproveVerifiableDomainPayload, graphql_name='approveVerifiableDomain', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveVerifiableDomainInput), graphql_name='input', default=None)),
))
    )
    archive_project_v2_item = sgqlc.types.Field(ArchiveProjectV2ItemPayload, graphql_name='archiveProjectV2Item', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ArchiveProjectV2ItemInput), graphql_name='input', default=None)),
))
    )
    archive_repository = sgqlc.types.Field(ArchiveRepositoryPayload, graphql_name='archiveRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ArchiveRepositoryInput), graphql_name='input', default=None)),
))
    )
    cancel_enterprise_admin_invitation = sgqlc.types.Field(CancelEnterpriseAdminInvitationPayload, graphql_name='cancelEnterpriseAdminInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CancelEnterpriseAdminInvitationInput), graphql_name='input', default=None)),
))
    )
    cancel_enterprise_member_invitation = sgqlc.types.Field(CancelEnterpriseMemberInvitationPayload, graphql_name='cancelEnterpriseMemberInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CancelEnterpriseMemberInvitationInput), graphql_name='input', default=None)),
))
    )
    cancel_sponsorship = sgqlc.types.Field(CancelSponsorshipPayload, graphql_name='cancelSponsorship', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CancelSponsorshipInput), graphql_name='input', default=None)),
))
    )
    change_user_status = sgqlc.types.Field(ChangeUserStatusPayload, graphql_name='changeUserStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeUserStatusInput), graphql_name='input', default=None)),
))
    )
    clear_labels_from_labelable = sgqlc.types.Field(ClearLabelsFromLabelablePayload, graphql_name='clearLabelsFromLabelable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ClearLabelsFromLabelableInput), graphql_name='input', default=None)),
))
    )
    clear_project_v2_item_field_value = sgqlc.types.Field(ClearProjectV2ItemFieldValuePayload, graphql_name='clearProjectV2ItemFieldValue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ClearProjectV2ItemFieldValueInput), graphql_name='input', default=None)),
))
    )
    clone_template_repository = sgqlc.types.Field(CloneTemplateRepositoryPayload, graphql_name='cloneTemplateRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloneTemplateRepositoryInput), graphql_name='input', default=None)),
))
    )
    close_discussion = sgqlc.types.Field(CloseDiscussionPayload, graphql_name='closeDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloseDiscussionInput), graphql_name='input', default=None)),
))
    )
    close_issue = sgqlc.types.Field(CloseIssuePayload, graphql_name='closeIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloseIssueInput), graphql_name='input', default=None)),
))
    )
    close_pull_request = sgqlc.types.Field(ClosePullRequestPayload, graphql_name='closePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ClosePullRequestInput), graphql_name='input', default=None)),
))
    )
    convert_project_v2_draft_issue_item_to_issue = sgqlc.types.Field(ConvertProjectV2DraftIssueItemToIssuePayload, graphql_name='convertProjectV2DraftIssueItemToIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConvertProjectV2DraftIssueItemToIssueInput), graphql_name='input', default=None)),
))
    )
    convert_pull_request_to_draft = sgqlc.types.Field(ConvertPullRequestToDraftPayload, graphql_name='convertPullRequestToDraft', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConvertPullRequestToDraftInput), graphql_name='input', default=None)),
))
    )
    copy_project_v2 = sgqlc.types.Field(CopyProjectV2Payload, graphql_name='copyProjectV2', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CopyProjectV2Input), graphql_name='input', default=None)),
))
    )
    create_attribution_invitation = sgqlc.types.Field(CreateAttributionInvitationPayload, graphql_name='createAttributionInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAttributionInvitationInput), graphql_name='input', default=None)),
))
    )
    create_branch_protection_rule = sgqlc.types.Field(CreateBranchProtectionRulePayload, graphql_name='createBranchProtectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBranchProtectionRuleInput), graphql_name='input', default=None)),
))
    )
    create_check_run = sgqlc.types.Field(CreateCheckRunPayload, graphql_name='createCheckRun', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCheckRunInput), graphql_name='input', default=None)),
))
    )
    create_check_suite = sgqlc.types.Field(CreateCheckSuitePayload, graphql_name='createCheckSuite', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCheckSuiteInput), graphql_name='input', default=None)),
))
    )
    create_commit_on_branch = sgqlc.types.Field(CreateCommitOnBranchPayload, graphql_name='createCommitOnBranch', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCommitOnBranchInput), graphql_name='input', default=None)),
))
    )
    create_deployment = sgqlc.types.Field(CreateDeploymentPayload, graphql_name='createDeployment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDeploymentInput), graphql_name='input', default=None)),
))
    )
    create_deployment_status = sgqlc.types.Field(CreateDeploymentStatusPayload, graphql_name='createDeploymentStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDeploymentStatusInput), graphql_name='input', default=None)),
))
    )
    create_discussion = sgqlc.types.Field(CreateDiscussionPayload, graphql_name='createDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDiscussionInput), graphql_name='input', default=None)),
))
    )
    create_enterprise_organization = sgqlc.types.Field(CreateEnterpriseOrganizationPayload, graphql_name='createEnterpriseOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnterpriseOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_environment = sgqlc.types.Field(CreateEnvironmentPayload, graphql_name='createEnvironment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnvironmentInput), graphql_name='input', default=None)),
))
    )
    create_ip_allow_list_entry = sgqlc.types.Field(CreateIpAllowListEntryPayload, graphql_name='createIpAllowListEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateIpAllowListEntryInput), graphql_name='input', default=None)),
))
    )
    create_issue = sgqlc.types.Field(CreateIssuePayload, graphql_name='createIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateIssueInput), graphql_name='input', default=None)),
))
    )
    create_issue_type = sgqlc.types.Field(CreateIssueTypePayload, graphql_name='createIssueType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateIssueTypeInput), graphql_name='input', default=None)),
))
    )
    create_label = sgqlc.types.Field(CreateLabelPayload, graphql_name='createLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateLabelInput), graphql_name='input', default=None)),
))
    )
    create_linked_branch = sgqlc.types.Field(CreateLinkedBranchPayload, graphql_name='createLinkedBranch', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateLinkedBranchInput), graphql_name='input', default=None)),
))
    )
    create_migration_source = sgqlc.types.Field(CreateMigrationSourcePayload, graphql_name='createMigrationSource', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMigrationSourceInput), graphql_name='input', default=None)),
))
    )
    create_project_v2 = sgqlc.types.Field(CreateProjectV2Payload, graphql_name='createProjectV2', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectV2Input), graphql_name='input', default=None)),
))
    )
    create_project_v2_field = sgqlc.types.Field(CreateProjectV2FieldPayload, graphql_name='createProjectV2Field', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectV2FieldInput), graphql_name='input', default=None)),
))
    )
    create_project_v2_status_update = sgqlc.types.Field(CreateProjectV2StatusUpdatePayload, graphql_name='createProjectV2StatusUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectV2StatusUpdateInput), graphql_name='input', default=None)),
))
    )
    create_pull_request = sgqlc.types.Field(CreatePullRequestPayload, graphql_name='createPullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePullRequestInput), graphql_name='input', default=None)),
))
    )
    create_ref = sgqlc.types.Field(CreateRefPayload, graphql_name='createRef', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRefInput), graphql_name='input', default=None)),
))
    )
    create_repository = sgqlc.types.Field(CreateRepositoryPayload, graphql_name='createRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRepositoryInput), graphql_name='input', default=None)),
))
    )
    create_repository_ruleset = sgqlc.types.Field(CreateRepositoryRulesetPayload, graphql_name='createRepositoryRuleset', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRepositoryRulesetInput), graphql_name='input', default=None)),
))
    )
    create_sponsors_listing = sgqlc.types.Field(CreateSponsorsListingPayload, graphql_name='createSponsorsListing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSponsorsListingInput), graphql_name='input', default=None)),
))
    )
    create_sponsors_tier = sgqlc.types.Field(CreateSponsorsTierPayload, graphql_name='createSponsorsTier', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSponsorsTierInput), graphql_name='input', default=None)),
))
    )
    create_sponsorship = sgqlc.types.Field(CreateSponsorshipPayload, graphql_name='createSponsorship', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSponsorshipInput), graphql_name='input', default=None)),
))
    )
    create_sponsorships = sgqlc.types.Field(CreateSponsorshipsPayload, graphql_name='createSponsorships', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSponsorshipsInput), graphql_name='input', default=None)),
))
    )
    create_team_discussion = sgqlc.types.Field(CreateTeamDiscussionPayload, graphql_name='createTeamDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTeamDiscussionInput), graphql_name='input', default=None)),
))
    )
    create_team_discussion_comment = sgqlc.types.Field(CreateTeamDiscussionCommentPayload, graphql_name='createTeamDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTeamDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    create_user_list = sgqlc.types.Field(CreateUserListPayload, graphql_name='createUserList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserListInput), graphql_name='input', default=None)),
))
    )
    decline_topic_suggestion = sgqlc.types.Field(DeclineTopicSuggestionPayload, graphql_name='declineTopicSuggestion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeclineTopicSuggestionInput), graphql_name='input', default=None)),
))
    )
    delete_branch_protection_rule = sgqlc.types.Field(DeleteBranchProtectionRulePayload, graphql_name='deleteBranchProtectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteBranchProtectionRuleInput), graphql_name='input', default=None)),
))
    )
    delete_deployment = sgqlc.types.Field(DeleteDeploymentPayload, graphql_name='deleteDeployment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteDeploymentInput), graphql_name='input', default=None)),
))
    )
    delete_discussion = sgqlc.types.Field(DeleteDiscussionPayload, graphql_name='deleteDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteDiscussionInput), graphql_name='input', default=None)),
))
    )
    delete_discussion_comment = sgqlc.types.Field(DeleteDiscussionCommentPayload, graphql_name='deleteDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    delete_environment = sgqlc.types.Field(DeleteEnvironmentPayload, graphql_name='deleteEnvironment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEnvironmentInput), graphql_name='input', default=None)),
))
    )
    delete_ip_allow_list_entry = sgqlc.types.Field(DeleteIpAllowListEntryPayload, graphql_name='deleteIpAllowListEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIpAllowListEntryInput), graphql_name='input', default=None)),
))
    )
    delete_issue = sgqlc.types.Field(DeleteIssuePayload, graphql_name='deleteIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIssueInput), graphql_name='input', default=None)),
))
    )
    delete_issue_comment = sgqlc.types.Field(DeleteIssueCommentPayload, graphql_name='deleteIssueComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIssueCommentInput), graphql_name='input', default=None)),
))
    )
    delete_issue_type = sgqlc.types.Field(DeleteIssueTypePayload, graphql_name='deleteIssueType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIssueTypeInput), graphql_name='input', default=None)),
))
    )
    delete_label = sgqlc.types.Field(DeleteLabelPayload, graphql_name='deleteLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteLabelInput), graphql_name='input', default=None)),
))
    )
    delete_linked_branch = sgqlc.types.Field(DeleteLinkedBranchPayload, graphql_name='deleteLinkedBranch', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteLinkedBranchInput), graphql_name='input', default=None)),
))
    )
    delete_package_version = sgqlc.types.Field(DeletePackageVersionPayload, graphql_name='deletePackageVersion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePackageVersionInput), graphql_name='input', default=None)),
))
    )
    delete_project_v2 = sgqlc.types.Field(DeleteProjectV2Payload, graphql_name='deleteProjectV2', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectV2Input), graphql_name='input', default=None)),
))
    )
    delete_project_v2_field = sgqlc.types.Field(DeleteProjectV2FieldPayload, graphql_name='deleteProjectV2Field', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectV2FieldInput), graphql_name='input', default=None)),
))
    )
    delete_project_v2_item = sgqlc.types.Field(DeleteProjectV2ItemPayload, graphql_name='deleteProjectV2Item', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectV2ItemInput), graphql_name='input', default=None)),
))
    )
    delete_project_v2_status_update = sgqlc.types.Field(DeleteProjectV2StatusUpdatePayload, graphql_name='deleteProjectV2StatusUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectV2StatusUpdateInput), graphql_name='input', default=None)),
))
    )
    delete_project_v2_workflow = sgqlc.types.Field(DeleteProjectV2WorkflowPayload, graphql_name='deleteProjectV2Workflow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectV2WorkflowInput), graphql_name='input', default=None)),
))
    )
    delete_pull_request_review = sgqlc.types.Field(DeletePullRequestReviewPayload, graphql_name='deletePullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    delete_pull_request_review_comment = sgqlc.types.Field(DeletePullRequestReviewCommentPayload, graphql_name='deletePullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    delete_ref = sgqlc.types.Field(DeleteRefPayload, graphql_name='deleteRef', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteRefInput), graphql_name='input', default=None)),
))
    )
    delete_repository_ruleset = sgqlc.types.Field(DeleteRepositoryRulesetPayload, graphql_name='deleteRepositoryRuleset', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteRepositoryRulesetInput), graphql_name='input', default=None)),
))
    )
    delete_team_discussion = sgqlc.types.Field(DeleteTeamDiscussionPayload, graphql_name='deleteTeamDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTeamDiscussionInput), graphql_name='input', default=None)),
))
    )
    delete_team_discussion_comment = sgqlc.types.Field(DeleteTeamDiscussionCommentPayload, graphql_name='deleteTeamDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTeamDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    delete_user_list = sgqlc.types.Field(DeleteUserListPayload, graphql_name='deleteUserList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserListInput), graphql_name='input', default=None)),
))
    )
    delete_verifiable_domain = sgqlc.types.Field(DeleteVerifiableDomainPayload, graphql_name='deleteVerifiableDomain', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteVerifiableDomainInput), graphql_name='input', default=None)),
))
    )
    dequeue_pull_request = sgqlc.types.Field(DequeuePullRequestPayload, graphql_name='dequeuePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DequeuePullRequestInput), graphql_name='input', default=None)),
))
    )
    disable_pull_request_auto_merge = sgqlc.types.Field(DisablePullRequestAutoMergePayload, graphql_name='disablePullRequestAutoMerge', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DisablePullRequestAutoMergeInput), graphql_name='input', default=None)),
))
    )
    dismiss_pull_request_review = sgqlc.types.Field(DismissPullRequestReviewPayload, graphql_name='dismissPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DismissPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    dismiss_repository_vulnerability_alert = sgqlc.types.Field(DismissRepositoryVulnerabilityAlertPayload, graphql_name='dismissRepositoryVulnerabilityAlert', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DismissRepositoryVulnerabilityAlertInput), graphql_name='input', default=None)),
))
    )
    enable_pull_request_auto_merge = sgqlc.types.Field(EnablePullRequestAutoMergePayload, graphql_name='enablePullRequestAutoMerge', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EnablePullRequestAutoMergeInput), graphql_name='input', default=None)),
))
    )
    enqueue_pull_request = sgqlc.types.Field(EnqueuePullRequestPayload, graphql_name='enqueuePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EnqueuePullRequestInput), graphql_name='input', default=None)),
))
    )
    follow_organization = sgqlc.types.Field(FollowOrganizationPayload, graphql_name='followOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FollowOrganizationInput), graphql_name='input', default=None)),
))
    )
    follow_user = sgqlc.types.Field(FollowUserPayload, graphql_name='followUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FollowUserInput), graphql_name='input', default=None)),
))
    )
    grant_enterprise_organizations_migrator_role = sgqlc.types.Field(GrantEnterpriseOrganizationsMigratorRolePayload, graphql_name='grantEnterpriseOrganizationsMigratorRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GrantEnterpriseOrganizationsMigratorRoleInput), graphql_name='input', default=None)),
))
    )
    grant_migrator_role = sgqlc.types.Field(GrantMigratorRolePayload, graphql_name='grantMigratorRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GrantMigratorRoleInput), graphql_name='input', default=None)),
))
    )
    invite_enterprise_admin = sgqlc.types.Field(InviteEnterpriseAdminPayload, graphql_name='inviteEnterpriseAdmin', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InviteEnterpriseAdminInput), graphql_name='input', default=None)),
))
    )
    invite_enterprise_member = sgqlc.types.Field(InviteEnterpriseMemberPayload, graphql_name='inviteEnterpriseMember', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InviteEnterpriseMemberInput), graphql_name='input', default=None)),
))
    )
    link_project_v2_to_repository = sgqlc.types.Field(LinkProjectV2ToRepositoryPayload, graphql_name='linkProjectV2ToRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LinkProjectV2ToRepositoryInput), graphql_name='input', default=None)),
))
    )
    link_project_v2_to_team = sgqlc.types.Field(LinkProjectV2ToTeamPayload, graphql_name='linkProjectV2ToTeam', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LinkProjectV2ToTeamInput), graphql_name='input', default=None)),
))
    )
    lock_lockable = sgqlc.types.Field(LockLockablePayload, graphql_name='lockLockable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LockLockableInput), graphql_name='input', default=None)),
))
    )
    mark_discussion_comment_as_answer = sgqlc.types.Field(MarkDiscussionCommentAsAnswerPayload, graphql_name='markDiscussionCommentAsAnswer', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MarkDiscussionCommentAsAnswerInput), graphql_name='input', default=None)),
))
    )
    mark_file_as_viewed = sgqlc.types.Field(MarkFileAsViewedPayload, graphql_name='markFileAsViewed', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MarkFileAsViewedInput), graphql_name='input', default=None)),
))
    )
    mark_project_v2_as_template = sgqlc.types.Field(MarkProjectV2AsTemplatePayload, graphql_name='markProjectV2AsTemplate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MarkProjectV2AsTemplateInput), graphql_name='input', default=None)),
))
    )
    mark_pull_request_ready_for_review = sgqlc.types.Field(MarkPullRequestReadyForReviewPayload, graphql_name='markPullRequestReadyForReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MarkPullRequestReadyForReviewInput), graphql_name='input', default=None)),
))
    )
    merge_branch = sgqlc.types.Field(MergeBranchPayload, graphql_name='mergeBranch', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MergeBranchInput), graphql_name='input', default=None)),
))
    )
    merge_pull_request = sgqlc.types.Field(MergePullRequestPayload, graphql_name='mergePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MergePullRequestInput), graphql_name='input', default=None)),
))
    )
    minimize_comment = sgqlc.types.Field(MinimizeCommentPayload, graphql_name='minimizeComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MinimizeCommentInput), graphql_name='input', default=None)),
))
    )
    pin_environment = sgqlc.types.Field('PinEnvironmentPayload', graphql_name='pinEnvironment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PinEnvironmentInput), graphql_name='input', default=None)),
))
    )
    pin_issue = sgqlc.types.Field('PinIssuePayload', graphql_name='pinIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PinIssueInput), graphql_name='input', default=None)),
))
    )
    publish_sponsors_tier = sgqlc.types.Field('PublishSponsorsTierPayload', graphql_name='publishSponsorsTier', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PublishSponsorsTierInput), graphql_name='input', default=None)),
))
    )
    regenerate_enterprise_identity_provider_recovery_codes = sgqlc.types.Field('RegenerateEnterpriseIdentityProviderRecoveryCodesPayload', graphql_name='regenerateEnterpriseIdentityProviderRecoveryCodes', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegenerateEnterpriseIdentityProviderRecoveryCodesInput), graphql_name='input', default=None)),
))
    )
    regenerate_verifiable_domain_token = sgqlc.types.Field('RegenerateVerifiableDomainTokenPayload', graphql_name='regenerateVerifiableDomainToken', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegenerateVerifiableDomainTokenInput), graphql_name='input', default=None)),
))
    )
    reject_deployments = sgqlc.types.Field('RejectDeploymentsPayload', graphql_name='rejectDeployments', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectDeploymentsInput), graphql_name='input', default=None)),
))
    )
    remove_assignees_from_assignable = sgqlc.types.Field('RemoveAssigneesFromAssignablePayload', graphql_name='removeAssigneesFromAssignable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveAssigneesFromAssignableInput), graphql_name='input', default=None)),
))
    )
    remove_blocked_by = sgqlc.types.Field('RemoveBlockedByPayload', graphql_name='removeBlockedBy', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveBlockedByInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_admin = sgqlc.types.Field('RemoveEnterpriseAdminPayload', graphql_name='removeEnterpriseAdmin', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseAdminInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_identity_provider = sgqlc.types.Field('RemoveEnterpriseIdentityProviderPayload', graphql_name='removeEnterpriseIdentityProvider', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseIdentityProviderInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_member = sgqlc.types.Field('RemoveEnterpriseMemberPayload', graphql_name='removeEnterpriseMember', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseMemberInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_organization = sgqlc.types.Field('RemoveEnterpriseOrganizationPayload', graphql_name='removeEnterpriseOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseOrganizationInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_support_entitlement = sgqlc.types.Field('RemoveEnterpriseSupportEntitlementPayload', graphql_name='removeEnterpriseSupportEntitlement', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseSupportEntitlementInput), graphql_name='input', default=None)),
))
    )
    remove_labels_from_labelable = sgqlc.types.Field('RemoveLabelsFromLabelablePayload', graphql_name='removeLabelsFromLabelable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveLabelsFromLabelableInput), graphql_name='input', default=None)),
))
    )
    remove_outside_collaborator = sgqlc.types.Field('RemoveOutsideCollaboratorPayload', graphql_name='removeOutsideCollaborator', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveOutsideCollaboratorInput), graphql_name='input', default=None)),
))
    )
    remove_reaction = sgqlc.types.Field('RemoveReactionPayload', graphql_name='removeReaction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveReactionInput), graphql_name='input', default=None)),
))
    )
    remove_star = sgqlc.types.Field('RemoveStarPayload', graphql_name='removeStar', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveStarInput), graphql_name='input', default=None)),
))
    )
    remove_sub_issue = sgqlc.types.Field('RemoveSubIssuePayload', graphql_name='removeSubIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveSubIssueInput), graphql_name='input', default=None)),
))
    )
    remove_upvote = sgqlc.types.Field('RemoveUpvotePayload', graphql_name='removeUpvote', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveUpvoteInput), graphql_name='input', default=None)),
))
    )
    reopen_discussion = sgqlc.types.Field('ReopenDiscussionPayload', graphql_name='reopenDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReopenDiscussionInput), graphql_name='input', default=None)),
))
    )
    reopen_issue = sgqlc.types.Field('ReopenIssuePayload', graphql_name='reopenIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReopenIssueInput), graphql_name='input', default=None)),
))
    )
    reopen_pull_request = sgqlc.types.Field('ReopenPullRequestPayload', graphql_name='reopenPullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReopenPullRequestInput), graphql_name='input', default=None)),
))
    )
    reorder_environment = sgqlc.types.Field('ReorderEnvironmentPayload', graphql_name='reorderEnvironment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReorderEnvironmentInput), graphql_name='input', default=None)),
))
    )
    replace_actors_for_assignable = sgqlc.types.Field('ReplaceActorsForAssignablePayload', graphql_name='replaceActorsForAssignable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReplaceActorsForAssignableInput), graphql_name='input', default=None)),
))
    )
    reprioritize_sub_issue = sgqlc.types.Field('ReprioritizeSubIssuePayload', graphql_name='reprioritizeSubIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReprioritizeSubIssueInput), graphql_name='input', default=None)),
))
    )
    request_reviews = sgqlc.types.Field('RequestReviewsPayload', graphql_name='requestReviews', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RequestReviewsInput), graphql_name='input', default=None)),
))
    )
    rerequest_check_suite = sgqlc.types.Field('RerequestCheckSuitePayload', graphql_name='rerequestCheckSuite', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RerequestCheckSuiteInput), graphql_name='input', default=None)),
))
    )
    resolve_review_thread = sgqlc.types.Field('ResolveReviewThreadPayload', graphql_name='resolveReviewThread', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ResolveReviewThreadInput), graphql_name='input', default=None)),
))
    )
    retire_sponsors_tier = sgqlc.types.Field('RetireSponsorsTierPayload', graphql_name='retireSponsorsTier', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RetireSponsorsTierInput), graphql_name='input', default=None)),
))
    )
    revert_pull_request = sgqlc.types.Field('RevertPullRequestPayload', graphql_name='revertPullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RevertPullRequestInput), graphql_name='input', default=None)),
))
    )
    revoke_enterprise_organizations_migrator_role = sgqlc.types.Field('RevokeEnterpriseOrganizationsMigratorRolePayload', graphql_name='revokeEnterpriseOrganizationsMigratorRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RevokeEnterpriseOrganizationsMigratorRoleInput), graphql_name='input', default=None)),
))
    )
    revoke_migrator_role = sgqlc.types.Field('RevokeMigratorRolePayload', graphql_name='revokeMigratorRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RevokeMigratorRoleInput), graphql_name='input', default=None)),
))
    )
    set_enterprise_identity_provider = sgqlc.types.Field('SetEnterpriseIdentityProviderPayload', graphql_name='setEnterpriseIdentityProvider', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetEnterpriseIdentityProviderInput), graphql_name='input', default=None)),
))
    )
    set_organization_interaction_limit = sgqlc.types.Field('SetOrganizationInteractionLimitPayload', graphql_name='setOrganizationInteractionLimit', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetOrganizationInteractionLimitInput), graphql_name='input', default=None)),
))
    )
    set_repository_interaction_limit = sgqlc.types.Field('SetRepositoryInteractionLimitPayload', graphql_name='setRepositoryInteractionLimit', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetRepositoryInteractionLimitInput), graphql_name='input', default=None)),
))
    )
    set_user_interaction_limit = sgqlc.types.Field('SetUserInteractionLimitPayload', graphql_name='setUserInteractionLimit', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetUserInteractionLimitInput), graphql_name='input', default=None)),
))
    )
    start_organization_migration = sgqlc.types.Field('StartOrganizationMigrationPayload', graphql_name='startOrganizationMigration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StartOrganizationMigrationInput), graphql_name='input', default=None)),
))
    )
    start_repository_migration = sgqlc.types.Field('StartRepositoryMigrationPayload', graphql_name='startRepositoryMigration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StartRepositoryMigrationInput), graphql_name='input', default=None)),
))
    )
    submit_pull_request_review = sgqlc.types.Field('SubmitPullRequestReviewPayload', graphql_name='submitPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SubmitPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    transfer_enterprise_organization = sgqlc.types.Field('TransferEnterpriseOrganizationPayload', graphql_name='transferEnterpriseOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TransferEnterpriseOrganizationInput), graphql_name='input', default=None)),
))
    )
    transfer_issue = sgqlc.types.Field('TransferIssuePayload', graphql_name='transferIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TransferIssueInput), graphql_name='input', default=None)),
))
    )
    unarchive_project_v2_item = sgqlc.types.Field('UnarchiveProjectV2ItemPayload', graphql_name='unarchiveProjectV2Item', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnarchiveProjectV2ItemInput), graphql_name='input', default=None)),
))
    )
    unarchive_repository = sgqlc.types.Field('UnarchiveRepositoryPayload', graphql_name='unarchiveRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnarchiveRepositoryInput), graphql_name='input', default=None)),
))
    )
    unfollow_organization = sgqlc.types.Field('UnfollowOrganizationPayload', graphql_name='unfollowOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnfollowOrganizationInput), graphql_name='input', default=None)),
))
    )
    unfollow_user = sgqlc.types.Field('UnfollowUserPayload', graphql_name='unfollowUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnfollowUserInput), graphql_name='input', default=None)),
))
    )
    unlink_project_v2_from_repository = sgqlc.types.Field('UnlinkProjectV2FromRepositoryPayload', graphql_name='unlinkProjectV2FromRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnlinkProjectV2FromRepositoryInput), graphql_name='input', default=None)),
))
    )
    unlink_project_v2_from_team = sgqlc.types.Field('UnlinkProjectV2FromTeamPayload', graphql_name='unlinkProjectV2FromTeam', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnlinkProjectV2FromTeamInput), graphql_name='input', default=None)),
))
    )
    unlock_lockable = sgqlc.types.Field('UnlockLockablePayload', graphql_name='unlockLockable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnlockLockableInput), graphql_name='input', default=None)),
))
    )
    unmark_discussion_comment_as_answer = sgqlc.types.Field('UnmarkDiscussionCommentAsAnswerPayload', graphql_name='unmarkDiscussionCommentAsAnswer', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnmarkDiscussionCommentAsAnswerInput), graphql_name='input', default=None)),
))
    )
    unmark_file_as_viewed = sgqlc.types.Field('UnmarkFileAsViewedPayload', graphql_name='unmarkFileAsViewed', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnmarkFileAsViewedInput), graphql_name='input', default=None)),
))
    )
    unmark_issue_as_duplicate = sgqlc.types.Field('UnmarkIssueAsDuplicatePayload', graphql_name='unmarkIssueAsDuplicate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnmarkIssueAsDuplicateInput), graphql_name='input', default=None)),
))
    )
    unmark_project_v2_as_template = sgqlc.types.Field('UnmarkProjectV2AsTemplatePayload', graphql_name='unmarkProjectV2AsTemplate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnmarkProjectV2AsTemplateInput), graphql_name='input', default=None)),
))
    )
    unminimize_comment = sgqlc.types.Field('UnminimizeCommentPayload', graphql_name='unminimizeComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnminimizeCommentInput), graphql_name='input', default=None)),
))
    )
    unpin_issue = sgqlc.types.Field('UnpinIssuePayload', graphql_name='unpinIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnpinIssueInput), graphql_name='input', default=None)),
))
    )
    unresolve_review_thread = sgqlc.types.Field('UnresolveReviewThreadPayload', graphql_name='unresolveReviewThread', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnresolveReviewThreadInput), graphql_name='input', default=None)),
))
    )
    update_branch_protection_rule = sgqlc.types.Field('UpdateBranchProtectionRulePayload', graphql_name='updateBranchProtectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBranchProtectionRuleInput), graphql_name='input', default=None)),
))
    )
    update_check_run = sgqlc.types.Field('UpdateCheckRunPayload', graphql_name='updateCheckRun', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCheckRunInput), graphql_name='input', default=None)),
))
    )
    update_check_suite_preferences = sgqlc.types.Field('UpdateCheckSuitePreferencesPayload', graphql_name='updateCheckSuitePreferences', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCheckSuitePreferencesInput), graphql_name='input', default=None)),
))
    )
    update_discussion = sgqlc.types.Field('UpdateDiscussionPayload', graphql_name='updateDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDiscussionInput), graphql_name='input', default=None)),
))
    )
    update_discussion_comment = sgqlc.types.Field('UpdateDiscussionCommentPayload', graphql_name='updateDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_administrator_role = sgqlc.types.Field('UpdateEnterpriseAdministratorRolePayload', graphql_name='updateEnterpriseAdministratorRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseAdministratorRoleInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_allow_private_repository_forking_setting = sgqlc.types.Field('UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload', graphql_name='updateEnterpriseAllowPrivateRepositoryForkingSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_default_repository_permission_setting = sgqlc.types.Field('UpdateEnterpriseDefaultRepositoryPermissionSettingPayload', graphql_name='updateEnterpriseDefaultRepositoryPermissionSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseDefaultRepositoryPermissionSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_deploy_key_setting = sgqlc.types.Field('UpdateEnterpriseDeployKeySettingPayload', graphql_name='updateEnterpriseDeployKeySetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseDeployKeySettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_change_repository_visibility_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload', graphql_name='updateEnterpriseMembersCanChangeRepositoryVisibilitySetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_create_repositories_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload', graphql_name='updateEnterpriseMembersCanCreateRepositoriesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanCreateRepositoriesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_delete_issues_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanDeleteIssuesSettingPayload', graphql_name='updateEnterpriseMembersCanDeleteIssuesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanDeleteIssuesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_delete_repositories_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload', graphql_name='updateEnterpriseMembersCanDeleteRepositoriesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_invite_collaborators_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload', graphql_name='updateEnterpriseMembersCanInviteCollaboratorsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_make_purchases_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanMakePurchasesSettingPayload', graphql_name='updateEnterpriseMembersCanMakePurchasesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanMakePurchasesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_update_protected_branches_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload', graphql_name='updateEnterpriseMembersCanUpdateProtectedBranchesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_view_dependency_insights_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload', graphql_name='updateEnterpriseMembersCanViewDependencyInsightsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_organization_projects_setting = sgqlc.types.Field('UpdateEnterpriseOrganizationProjectsSettingPayload', graphql_name='updateEnterpriseOrganizationProjectsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseOrganizationProjectsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_owner_organization_role = sgqlc.types.Field('UpdateEnterpriseOwnerOrganizationRolePayload', graphql_name='updateEnterpriseOwnerOrganizationRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseOwnerOrganizationRoleInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_profile = sgqlc.types.Field('UpdateEnterpriseProfilePayload', graphql_name='updateEnterpriseProfile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseProfileInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_repository_projects_setting = sgqlc.types.Field('UpdateEnterpriseRepositoryProjectsSettingPayload', graphql_name='updateEnterpriseRepositoryProjectsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseRepositoryProjectsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_team_discussions_setting = sgqlc.types.Field('UpdateEnterpriseTeamDiscussionsSettingPayload', graphql_name='updateEnterpriseTeamDiscussionsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseTeamDiscussionsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_two_factor_authentication_disallowed_methods_setting = sgqlc.types.Field('UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSettingPayload', graphql_name='updateEnterpriseTwoFactorAuthenticationDisallowedMethodsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_two_factor_authentication_required_setting = sgqlc.types.Field('UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload', graphql_name='updateEnterpriseTwoFactorAuthenticationRequiredSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput), graphql_name='input', default=None)),
))
    )
    update_environment = sgqlc.types.Field('UpdateEnvironmentPayload', graphql_name='updateEnvironment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnvironmentInput), graphql_name='input', default=None)),
))
    )
    update_ip_allow_list_enabled_setting = sgqlc.types.Field('UpdateIpAllowListEnabledSettingPayload', graphql_name='updateIpAllowListEnabledSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIpAllowListEnabledSettingInput), graphql_name='input', default=None)),
))
    )
    update_ip_allow_list_entry = sgqlc.types.Field('UpdateIpAllowListEntryPayload', graphql_name='updateIpAllowListEntry', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIpAllowListEntryInput), graphql_name='input', default=None)),
))
    )
    update_ip_allow_list_for_installed_apps_enabled_setting = sgqlc.types.Field('UpdateIpAllowListForInstalledAppsEnabledSettingPayload', graphql_name='updateIpAllowListForInstalledAppsEnabledSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIpAllowListForInstalledAppsEnabledSettingInput), graphql_name='input', default=None)),
))
    )
    update_issue = sgqlc.types.Field('UpdateIssuePayload', graphql_name='updateIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueInput), graphql_name='input', default=None)),
))
    )
    update_issue_comment = sgqlc.types.Field('UpdateIssueCommentPayload', graphql_name='updateIssueComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueCommentInput), graphql_name='input', default=None)),
))
    )
    update_issue_issue_type = sgqlc.types.Field('UpdateIssueIssueTypePayload', graphql_name='updateIssueIssueType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueIssueTypeInput), graphql_name='input', default=None)),
))
    )
    update_issue_type = sgqlc.types.Field('UpdateIssueTypePayload', graphql_name='updateIssueType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueTypeInput), graphql_name='input', default=None)),
))
    )
    update_label = sgqlc.types.Field('UpdateLabelPayload', graphql_name='updateLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLabelInput), graphql_name='input', default=None)),
))
    )
    update_notification_restriction_setting = sgqlc.types.Field('UpdateNotificationRestrictionSettingPayload', graphql_name='updateNotificationRestrictionSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateNotificationRestrictionSettingInput), graphql_name='input', default=None)),
))
    )
    update_organization_allow_private_repository_forking_setting = sgqlc.types.Field('UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload', graphql_name='updateOrganizationAllowPrivateRepositoryForkingSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationAllowPrivateRepositoryForkingSettingInput), graphql_name='input', default=None)),
))
    )
    update_organization_web_commit_signoff_setting = sgqlc.types.Field('UpdateOrganizationWebCommitSignoffSettingPayload', graphql_name='updateOrganizationWebCommitSignoffSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizationWebCommitSignoffSettingInput), graphql_name='input', default=None)),
))
    )
    update_patreon_sponsorability = sgqlc.types.Field('UpdatePatreonSponsorabilityPayload', graphql_name='updatePatreonSponsorability', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePatreonSponsorabilityInput), graphql_name='input', default=None)),
))
    )
    update_project_v2 = sgqlc.types.Field('UpdateProjectV2Payload', graphql_name='updateProjectV2', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2Input), graphql_name='input', default=None)),
))
    )
    update_project_v2_collaborators = sgqlc.types.Field('UpdateProjectV2CollaboratorsPayload', graphql_name='updateProjectV2Collaborators', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2CollaboratorsInput), graphql_name='input', default=None)),
))
    )
    update_project_v2_draft_issue = sgqlc.types.Field('UpdateProjectV2DraftIssuePayload', graphql_name='updateProjectV2DraftIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2DraftIssueInput), graphql_name='input', default=None)),
))
    )
    update_project_v2_field = sgqlc.types.Field('UpdateProjectV2FieldPayload', graphql_name='updateProjectV2Field', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2FieldInput), graphql_name='input', default=None)),
))
    )
    update_project_v2_item_field_value = sgqlc.types.Field('UpdateProjectV2ItemFieldValuePayload', graphql_name='updateProjectV2ItemFieldValue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2ItemFieldValueInput), graphql_name='input', default=None)),
))
    )
    update_project_v2_item_position = sgqlc.types.Field('UpdateProjectV2ItemPositionPayload', graphql_name='updateProjectV2ItemPosition', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2ItemPositionInput), graphql_name='input', default=None)),
))
    )
    update_project_v2_status_update = sgqlc.types.Field('UpdateProjectV2StatusUpdatePayload', graphql_name='updateProjectV2StatusUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectV2StatusUpdateInput), graphql_name='input', default=None)),
))
    )
    update_pull_request = sgqlc.types.Field('UpdatePullRequestPayload', graphql_name='updatePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_branch = sgqlc.types.Field('UpdatePullRequestBranchPayload', graphql_name='updatePullRequestBranch', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestBranchInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_review = sgqlc.types.Field('UpdatePullRequestReviewPayload', graphql_name='updatePullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_review_comment = sgqlc.types.Field('UpdatePullRequestReviewCommentPayload', graphql_name='updatePullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    update_ref = sgqlc.types.Field('UpdateRefPayload', graphql_name='updateRef', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRefInput), graphql_name='input', default=None)),
))
    )
    update_refs = sgqlc.types.Field('UpdateRefsPayload', graphql_name='updateRefs', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRefsInput), graphql_name='input', default=None)),
))
    )
    update_repository = sgqlc.types.Field('UpdateRepositoryPayload', graphql_name='updateRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRepositoryInput), graphql_name='input', default=None)),
))
    )
    update_repository_ruleset = sgqlc.types.Field('UpdateRepositoryRulesetPayload', graphql_name='updateRepositoryRuleset', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRepositoryRulesetInput), graphql_name='input', default=None)),
))
    )
    update_repository_web_commit_signoff_setting = sgqlc.types.Field('UpdateRepositoryWebCommitSignoffSettingPayload', graphql_name='updateRepositoryWebCommitSignoffSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRepositoryWebCommitSignoffSettingInput), graphql_name='input', default=None)),
))
    )
    update_sponsorship_preferences = sgqlc.types.Field('UpdateSponsorshipPreferencesPayload', graphql_name='updateSponsorshipPreferences', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSponsorshipPreferencesInput), graphql_name='input', default=None)),
))
    )
    update_subscription = sgqlc.types.Field('UpdateSubscriptionPayload', graphql_name='updateSubscription', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSubscriptionInput), graphql_name='input', default=None)),
))
    )
    update_team_discussion = sgqlc.types.Field('UpdateTeamDiscussionPayload', graphql_name='updateTeamDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTeamDiscussionInput), graphql_name='input', default=None)),
))
    )
    update_team_discussion_comment = sgqlc.types.Field('UpdateTeamDiscussionCommentPayload', graphql_name='updateTeamDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTeamDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    update_team_review_assignment = sgqlc.types.Field('UpdateTeamReviewAssignmentPayload', graphql_name='updateTeamReviewAssignment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTeamReviewAssignmentInput), graphql_name='input', default=None)),
))
    )
    update_teams_repository = sgqlc.types.Field('UpdateTeamsRepositoryPayload', graphql_name='updateTeamsRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTeamsRepositoryInput), graphql_name='input', default=None)),
))
    )
    update_topics = sgqlc.types.Field('UpdateTopicsPayload', graphql_name='updateTopics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTopicsInput), graphql_name='input', default=None)),
))
    )
    update_user_list = sgqlc.types.Field('UpdateUserListPayload', graphql_name='updateUserList', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserListInput), graphql_name='input', default=None)),
))
    )
    update_user_lists_for_item = sgqlc.types.Field('UpdateUserListsForItemPayload', graphql_name='updateUserListsForItem', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserListsForItemInput), graphql_name='input', default=None)),
))
    )
    verify_verifiable_domain = sgqlc.types.Field('VerifyVerifiableDomainPayload', graphql_name='verifyVerifiableDomain', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(VerifyVerifiableDomainInput), graphql_name='input', default=None)),
))
    )


class OrganizationAuditEntryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationAuditEntryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationAuditEntry'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationAuditEntryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationAuditEntry', graphql_name='node')


class OrganizationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')


class OrganizationEnterpriseOwnerConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationEnterpriseOwnerEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationEnterpriseOwnerEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'organization_role')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    organization_role = sgqlc.types.Field(sgqlc.types.non_null(RoleInOrganization), graphql_name='organizationRole')


class OrganizationInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationInvitationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationInvitation', graphql_name='node')


class OrganizationMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationMemberEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'has_two_factor_enabled', 'node', 'role')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    has_two_factor_enabled = sgqlc.types.Field(Boolean, graphql_name='hasTwoFactorEnabled')
    node = sgqlc.types.Field('User', graphql_name='node')
    role = sgqlc.types.Field(OrganizationMemberRole, graphql_name='role')


class OrganizationPropertyConditionTarget(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('exclude', 'include')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationPropertyTargetDefinition'))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationPropertyTargetDefinition'))), graphql_name='include')


class OrganizationPropertyTargetDefinition(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'property_values')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='propertyValues')


class PackageConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PackageEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Package'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PackageEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Package', graphql_name='node')


class PackageFileConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PackageFileEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PackageFile'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PackageFileEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PackageFile', graphql_name='node')


class PackageStatistics(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('downloads_total_count',)
    downloads_total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadsTotalCount')


class PackageVersionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PackageVersionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PackageVersion'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PackageVersionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PackageVersion', graphql_name='node')


class PackageVersionStatistics(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('downloads_total_count',)
    downloads_total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadsTotalCount')


class PageInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class PermissionSource(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organization', 'permission', 'role_name', 'source')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    permission = sgqlc.types.Field(sgqlc.types.non_null(DefaultRepositoryPermissionField), graphql_name='permission')
    role_name = sgqlc.types.Field(String, graphql_name='roleName')
    source = sgqlc.types.Field(sgqlc.types.non_null('PermissionGranter'), graphql_name='source')


class PinEnvironmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment', 'pinned_environment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment = sgqlc.types.Field('Environment', graphql_name='environment')
    pinned_environment = sgqlc.types.Field('PinnedEnvironment', graphql_name='pinnedEnvironment')


class PinIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class PinnableItemConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PinnableItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PinnableItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PinnableItemEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PinnableItem', graphql_name='node')


class PinnedDiscussionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PinnedDiscussionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PinnedDiscussion'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PinnedDiscussionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PinnedDiscussion', graphql_name='node')


class PinnedEnvironmentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PinnedEnvironmentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PinnedEnvironment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PinnedEnvironmentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PinnedEnvironment', graphql_name='node')


class PinnedIssueConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PinnedIssueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PinnedIssue'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PinnedIssueEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PinnedIssue', graphql_name='node')


class ProfileItemShowcase(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_pinned_items', 'items')
    has_pinned_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPinnedItems')
    items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ProjectCardConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectCardEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectCard'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectCardEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectCard', graphql_name='node')


class ProjectColumnConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectColumnEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectColumn'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectColumnEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectColumn', graphql_name='node')


class ProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Project'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')


class ProjectProgress(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ()


class ProjectV2ActorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2ActorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2Actor'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2ActorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2Actor', graphql_name='node')


class ProjectV2Connection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2Edge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2Edge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2', graphql_name='node')


class ProjectV2FieldConfigurationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2FieldConfigurationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2FieldConfiguration'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2FieldConfigurationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2FieldConfiguration', graphql_name='node')


class ProjectV2FieldConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2FieldEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2Field'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2FieldEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2Field', graphql_name='node')


class ProjectV2ItemConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2ItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2Item'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2ItemEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2Item', graphql_name='node')


class ProjectV2ItemFieldLabelValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'labels')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ProjectV2ItemFieldMilestoneValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'milestone')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone')


class ProjectV2ItemFieldPullRequestValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'pull_requests')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    pull_requests = sgqlc.types.Field('PullRequestConnection', graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(PullRequestOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )


class ProjectV2ItemFieldRepositoryValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'repository')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class ProjectV2ItemFieldReviewerValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'reviewers')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    reviewers = sgqlc.types.Field('RequestedReviewerConnection', graphql_name='reviewers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ProjectV2ItemFieldUserValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'users')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')
    users = sgqlc.types.Field('UserConnection', graphql_name='users', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ProjectV2ItemFieldValueConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2ItemFieldValueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2ItemFieldValue'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2ItemFieldValueEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2ItemFieldValue', graphql_name='node')


class ProjectV2IterationFieldConfiguration(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('completed_iterations', 'duration', 'iterations', 'start_day')
    completed_iterations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectV2IterationFieldIteration'))), graphql_name='completedIterations')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    iterations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectV2IterationFieldIteration'))), graphql_name='iterations')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startDay')


class ProjectV2IterationFieldIteration(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('duration', 'id', 'start_date', 'title', 'title_html')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='startDate')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    title_html = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='titleHTML')


class ProjectV2SingleSelectFieldOption(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('color', 'description', 'description_html', 'id', 'name', 'name_html')
    color = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2SingleSelectFieldOptionColor), graphql_name='color')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='descriptionHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_html = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameHTML')


class ProjectV2SortBy(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('direction', 'field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2Field'), graphql_name='field')


class ProjectV2SortByConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2SortByEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(ProjectV2SortBy), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2SortByEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(ProjectV2SortBy, graphql_name='node')


class ProjectV2SortByField(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('direction', 'field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')
    field = sgqlc.types.Field(sgqlc.types.non_null('ProjectV2FieldConfiguration'), graphql_name='field')


class ProjectV2SortByFieldConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2SortByFieldEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(ProjectV2SortByField), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2SortByFieldEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(ProjectV2SortByField, graphql_name='node')


class ProjectV2StatusUpdateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2StatusUpdateEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2StatusUpdate'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2StatusUpdateEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2StatusUpdate', graphql_name='node')


class ProjectV2ViewConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2ViewEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2View'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2ViewEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2View', graphql_name='node')


class ProjectV2WorkflowConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2WorkflowEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectV2Workflow'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectV2WorkflowEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectV2Workflow', graphql_name='node')


class PropertyTargetDefinition(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'property_values', 'source')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='propertyValues')
    source = sgqlc.types.Field(String, graphql_name='source')


class PublicKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PublicKeyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PublicKey'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PublicKeyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PublicKey', graphql_name='node')


class PublishSponsorsTierPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsors_tier')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsors_tier = sgqlc.types.Field('SponsorsTier', graphql_name='sponsorsTier')


class PullRequestChangedFile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('additions', 'change_type', 'deletions', 'path', 'viewer_viewed_state')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    change_type = sgqlc.types.Field(sgqlc.types.non_null(PatchStatus), graphql_name='changeType')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    viewer_viewed_state = sgqlc.types.Field(sgqlc.types.non_null(FileViewedState), graphql_name='viewerViewedState')


class PullRequestChangedFileConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestChangedFileEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(PullRequestChangedFile), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestChangedFileEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(PullRequestChangedFile, graphql_name='node')


class PullRequestCommitConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestCommitEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestCommit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestCommitEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestCommit', graphql_name='node')


class PullRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestContributionsByRepository(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('contributions', 'repository')
    contributions = sgqlc.types.Field(sgqlc.types.non_null(CreatedPullRequestContributionConnection), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PullRequestEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequest', graphql_name='node')


class PullRequestParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('allowed_merge_methods', 'automatic_copilot_code_review_enabled', 'dismiss_stale_reviews_on_push', 'require_code_owner_review', 'require_last_push_approval', 'required_approving_review_count', 'required_review_thread_resolution')
    allowed_merge_methods = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestAllowedMergeMethods)), graphql_name='allowedMergeMethods')
    automatic_copilot_code_review_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='automaticCopilotCodeReviewEnabled')
    dismiss_stale_reviews_on_push = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dismissStaleReviewsOnPush')
    require_code_owner_review = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requireCodeOwnerReview')
    require_last_push_approval = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requireLastPushApproval')
    required_approving_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='requiredApprovingReviewCount')
    required_review_thread_resolution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiredReviewThreadResolution')


class PullRequestReviewCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewCommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReviewComment', graphql_name='node')


class PullRequestReviewConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReview'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewContributionsByRepository(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('contributions', 'repository')
    contributions = sgqlc.types.Field(sgqlc.types.non_null(CreatedPullRequestReviewContributionConnection), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PullRequestReviewEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReview', graphql_name='node')


class PullRequestReviewThreadConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewThreadEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewThread'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewThreadEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReviewThread', graphql_name='node')


class PullRequestRevisionMarker(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('created_at', 'last_seen_commit', 'pull_request')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    last_seen_commit = sgqlc.types.Field(sgqlc.types.non_null('Commit'), graphql_name='lastSeenCommit')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class PullRequestTemplate(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('body', 'filename', 'repository')
    body = sgqlc.types.Field(String, graphql_name='body')
    filename = sgqlc.types.Field(String, graphql_name='filename')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PullRequestTimelineConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestTimelineItemEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestTimelineItem', graphql_name='node')


class PullRequestTimelineItemsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'filtered_count', 'nodes', 'page_count', 'page_info', 'total_count', 'updated_at')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItemsEdge'), graphql_name='edges')
    filtered_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filteredCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItems'), graphql_name='nodes')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PullRequestTimelineItemsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestTimelineItems', graphql_name='node')


class PushAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('PushAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PushAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PushAllowanceEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PushAllowance', graphql_name='node')


class RateLimit(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cost', 'limit', 'node_count', 'remaining', 'reset_at', 'used')
    cost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cost')
    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')
    node_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nodeCount')
    remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='remaining')
    reset_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='resetAt')
    used = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='used')


class ReactingUserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactingUserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReactingUserEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'reacted_at')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    reacted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='reactedAt')


class ReactionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count', 'viewer_has_reacted')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Reaction'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    viewer_has_reacted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasReacted')


class ReactionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Reaction', graphql_name='node')


class ReactionGroup(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('content', 'created_at', 'reactors', 'subject', 'viewer_has_reacted')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    reactors = sgqlc.types.Field(sgqlc.types.non_null('ReactorConnection'), graphql_name='reactors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    subject = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='subject')
    viewer_has_reacted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasReacted')


class ReactorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Reactor'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReactorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'reacted_at')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Reactor'), graphql_name='node')
    reacted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='reactedAt')


class RefConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RefEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Ref'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RefEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Ref', graphql_name='node')


class RefNameConditionTarget(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('exclude', 'include')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='include')


class RefUpdateRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('allows_deletions', 'allows_force_pushes', 'blocks_creations', 'pattern', 'required_approving_review_count', 'required_status_check_contexts', 'requires_code_owner_reviews', 'requires_conversation_resolution', 'requires_linear_history', 'requires_signatures', 'viewer_allowed_to_dismiss_reviews', 'viewer_can_push')
    allows_deletions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowsDeletions')
    allows_force_pushes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowsForcePushes')
    blocks_creations = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='blocksCreations')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='requiredStatusCheckContexts')
    requires_code_owner_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresCodeOwnerReviews')
    requires_conversation_resolution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresConversationResolution')
    requires_linear_history = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresLinearHistory')
    requires_signatures = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresSignatures')
    viewer_allowed_to_dismiss_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerAllowedToDismissReviews')
    viewer_can_push = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanPush')


class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'identity_provider')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    identity_provider = sgqlc.types.Field('EnterpriseIdentityProvider', graphql_name='identityProvider')


class RegenerateVerifiableDomainTokenPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'verification_token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    verification_token = sgqlc.types.Field(String, graphql_name='verificationToken')


class RejectDeploymentsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deployments')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deployments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Deployment')), graphql_name='deployments')


class ReleaseAssetConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReleaseAssetEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReleaseAsset'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseAssetEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReleaseAsset', graphql_name='node')


class ReleaseConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReleaseEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Release'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Release', graphql_name='node')


class RemoveAssigneesFromAssignablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assignable', 'client_mutation_id')
    assignable = sgqlc.types.Field(Assignable, graphql_name='assignable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveBlockedByPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('blocking_issue', 'client_mutation_id', 'issue')
    blocking_issue = sgqlc.types.Field('Issue', graphql_name='blockingIssue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class RemoveEnterpriseAdminPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('admin', 'client_mutation_id', 'enterprise', 'message', 'viewer')
    admin = sgqlc.types.Field('User', graphql_name='admin')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')
    viewer = sgqlc.types.Field('User', graphql_name='viewer')


class RemoveEnterpriseIdentityProviderPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'identity_provider')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    identity_provider = sgqlc.types.Field('EnterpriseIdentityProvider', graphql_name='identityProvider')


class RemoveEnterpriseMemberPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'user', 'viewer')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    user = sgqlc.types.Field('User', graphql_name='user')
    viewer = sgqlc.types.Field('User', graphql_name='viewer')


class RemoveEnterpriseOrganizationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'organization', 'viewer')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    viewer = sgqlc.types.Field('User', graphql_name='viewer')


class RemoveEnterpriseSupportEntitlementPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')


class RemoveLabelsFromLabelablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'labelable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable = sgqlc.types.Field(Labelable, graphql_name='labelable')


class RemoveOutsideCollaboratorPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'removed_user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    removed_user = sgqlc.types.Field('User', graphql_name='removedUser')


class RemoveReactionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'reaction', 'reaction_groups', 'subject')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    reaction = sgqlc.types.Field('Reaction', graphql_name='reaction')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    subject = sgqlc.types.Field(Reactable, graphql_name='subject')


class RemoveStarPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'starrable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable = sgqlc.types.Field(Starrable, graphql_name='starrable')


class RemoveSubIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue', 'sub_issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')
    sub_issue = sgqlc.types.Field('Issue', graphql_name='subIssue')


class RemoveUpvotePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject = sgqlc.types.Field(Votable, graphql_name='subject')


class ReopenDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class ReopenIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class ReopenPullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class ReorderEnvironmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment = sgqlc.types.Field('Environment', graphql_name='environment')


class ReplaceActorsForAssignablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assignable', 'client_mutation_id')
    assignable = sgqlc.types.Field(Assignable, graphql_name='assignable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RepositoryCodeowners(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('errors',)
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RepositoryCodeownersError'))), graphql_name='errors')


class RepositoryCodeownersError(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('column', 'kind', 'line', 'message', 'path', 'source', 'suggestion')
    column = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='column')
    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')
    line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='line')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    suggestion = sgqlc.types.Field(String, graphql_name='suggestion')


class RepositoryCollaboratorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryCollaboratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryCollaboratorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'permission', 'permission_sources')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')
    permission_sources = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionSource)), graphql_name='permissionSources')


class RepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count', 'total_disk_usage')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_disk_usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalDiskUsage')


class RepositoryContactLink(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('about', 'name', 'url')
    about = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='about')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RepositoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Repository', graphql_name='node')


class RepositoryIdConditionTarget(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('repository_ids',)
    repository_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='repositoryIds')


class RepositoryInteractionAbility(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('expires_at', 'limit', 'origin')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    limit = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInteractionLimit), graphql_name='limit')
    origin = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInteractionLimitOrigin), graphql_name='origin')


class RepositoryInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryInvitationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryInvitation', graphql_name='node')


class RepositoryMigrationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryMigrationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryMigration'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryMigrationEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryMigration', graphql_name='node')


class RepositoryNameConditionTarget(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('exclude', 'include', 'protected')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='include')
    protected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='protected')


class RepositoryPlanFeatures(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('codeowners', 'draft_pull_requests', 'maximum_assignees', 'maximum_manual_review_requests', 'team_review_requests')
    codeowners = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='codeowners')
    draft_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='draftPullRequests')
    maximum_assignees = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maximumAssignees')
    maximum_manual_review_requests = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maximumManualReviewRequests')
    team_review_requests = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='teamReviewRequests')


class RepositoryPropertyConditionTarget(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('exclude', 'include')
    exclude = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PropertyTargetDefinition))), graphql_name='exclude')
    include = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PropertyTargetDefinition))), graphql_name='include')


class RepositoryRuleConditions(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organization_property', 'ref_name', 'repository_id', 'repository_name', 'repository_property')
    organization_property = sgqlc.types.Field(OrganizationPropertyConditionTarget, graphql_name='organizationProperty')
    ref_name = sgqlc.types.Field(RefNameConditionTarget, graphql_name='refName')
    repository_id = sgqlc.types.Field(RepositoryIdConditionTarget, graphql_name='repositoryId')
    repository_name = sgqlc.types.Field(RepositoryNameConditionTarget, graphql_name='repositoryName')
    repository_property = sgqlc.types.Field(RepositoryPropertyConditionTarget, graphql_name='repositoryProperty')


class RepositoryRuleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryRuleEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryRule'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryRuleEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryRule', graphql_name='node')


class RepositoryRulesetBypassActorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryRulesetBypassActorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryRulesetBypassActor'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryRulesetBypassActorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryRulesetBypassActor', graphql_name='node')


class RepositoryRulesetConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryRulesetEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryRuleset'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryRulesetEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryRuleset', graphql_name='node')


class RepositoryTopicConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryTopicEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryTopic'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryTopicEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryTopic', graphql_name='node')


class RepositoryVulnerabilityAlertConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryVulnerabilityAlertEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryVulnerabilityAlert'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryVulnerabilityAlertEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryVulnerabilityAlert', graphql_name='node')


class ReprioritizeSubIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class RequestReviewsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'pull_request', 'requested_reviewers_edge')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    requested_reviewers_edge = sgqlc.types.Field('UserEdge', graphql_name='requestedReviewersEdge')


class RequestedReviewerConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('RequestedReviewerEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RequestedReviewer'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RequestedReviewerEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RequestedReviewer', graphql_name='node')


class RequiredDeploymentsParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('required_deployment_environments',)
    required_deployment_environments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='requiredDeploymentEnvironments')


class RequiredStatusCheckDescription(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('app', 'context')
    app = sgqlc.types.Field('App', graphql_name='app')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')


class RequiredStatusChecksParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('do_not_enforce_on_create', 'required_status_checks', 'strict_required_status_checks_policy')
    do_not_enforce_on_create = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doNotEnforceOnCreate')
    required_status_checks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatusCheckConfiguration'))), graphql_name='requiredStatusChecks')
    strict_required_status_checks_policy = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='strictRequiredStatusChecksPolicy')


class RerequestCheckSuitePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('check_suite', 'client_mutation_id')
    check_suite = sgqlc.types.Field('CheckSuite', graphql_name='checkSuite')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ResolveReviewThreadPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'thread')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread = sgqlc.types.Field('PullRequestReviewThread', graphql_name='thread')


class RetireSponsorsTierPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsors_tier')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsors_tier = sgqlc.types.Field('SponsorsTier', graphql_name='sponsorsTier')


class RevertPullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request', 'revert_pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    revert_pull_request = sgqlc.types.Field('PullRequest', graphql_name='revertPullRequest')


class ReviewDismissalAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReviewDismissalAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReviewDismissalAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewDismissalAllowanceEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReviewDismissalAllowance', graphql_name='node')


class ReviewRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReviewRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReviewRequest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewRequestEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReviewRequest', graphql_name='node')


class RevokeEnterpriseOrganizationsMigratorRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organizations')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organizations = sgqlc.types.Field(OrganizationConnection, graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class RevokeMigratorRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class SavedReplyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SavedReplyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SavedReply'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SavedReplyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SavedReply', graphql_name='node')


class SearchResultItemConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('code_count', 'discussion_count', 'edges', 'issue_count', 'nodes', 'page_info', 'repository_count', 'user_count', 'wiki_count')
    code_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='codeCount')
    discussion_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='discussionCount')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SearchResultItemEdge'), graphql_name='edges')
    issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issueCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SearchResultItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    repository_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryCount')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')
    wiki_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='wikiCount')


class SearchResultItemEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'text_matches')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SearchResultItem', graphql_name='node')
    text_matches = sgqlc.types.Field(sgqlc.types.list_of('TextMatch'), graphql_name='textMatches')


class SecurityAdvisoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SecurityAdvisoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SecurityAdvisory'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SecurityAdvisoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SecurityAdvisory', graphql_name='node')


class SecurityAdvisoryIdentifier(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'value')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class SecurityAdvisoryPackage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('ecosystem', 'name')
    ecosystem = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryEcosystem), graphql_name='ecosystem')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class SecurityAdvisoryPackageVersion(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('identifier',)
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')


class SecurityAdvisoryReference(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class SecurityVulnerability(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('advisory', 'first_patched_version', 'package', 'severity', 'updated_at', 'vulnerable_version_range')
    advisory = sgqlc.types.Field(sgqlc.types.non_null('SecurityAdvisory'), graphql_name='advisory')
    first_patched_version = sgqlc.types.Field(SecurityAdvisoryPackageVersion, graphql_name='firstPatchedVersion')
    package = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryPackage), graphql_name='package')
    severity = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisorySeverity), graphql_name='severity')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    vulnerable_version_range = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vulnerableVersionRange')


class SecurityVulnerabilityConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SecurityVulnerabilityEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(SecurityVulnerability), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SecurityVulnerabilityEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(SecurityVulnerability, graphql_name='node')


class SetEnterpriseIdentityProviderPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'identity_provider')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    identity_provider = sgqlc.types.Field('EnterpriseIdentityProvider', graphql_name='identityProvider')


class SetOrganizationInteractionLimitPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class SetRepositoryInteractionLimitPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class SetUserInteractionLimitPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class SocialAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('display_name', 'provider', 'url')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    provider = sgqlc.types.Field(sgqlc.types.non_null(SocialAccountProvider), graphql_name='provider')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class SocialAccountConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SocialAccountEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(SocialAccount), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SocialAccountEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(SocialAccount, graphql_name='node')


class SponsorAndLifetimeValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('amount_in_cents', 'formatted_amount', 'sponsor', 'sponsorable')
    amount_in_cents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amountInCents')
    formatted_amount = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='formattedAmount')
    sponsor = sgqlc.types.Field(sgqlc.types.non_null(Sponsorable), graphql_name='sponsor')
    sponsorable = sgqlc.types.Field(sgqlc.types.non_null(Sponsorable), graphql_name='sponsorable')


class SponsorAndLifetimeValueConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorAndLifetimeValueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(SponsorAndLifetimeValue), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorAndLifetimeValueEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(SponsorAndLifetimeValue, graphql_name='node')


class SponsorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Sponsor'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Sponsor', graphql_name='node')


class SponsorableItemConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorableItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SponsorableItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorableItemEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SponsorableItem', graphql_name='node')


class SponsorsActivityConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorsActivityEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SponsorsActivity'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorsActivityEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SponsorsActivity', graphql_name='node')


class SponsorsGoal(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('description', 'kind', 'percent_complete', 'target_value', 'title')
    description = sgqlc.types.Field(String, graphql_name='description')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SponsorsGoalKind), graphql_name='kind')
    percent_complete = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='percentComplete')
    target_value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='targetValue')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class SponsorsTierAdminInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('is_draft', 'is_published', 'is_retired', 'sponsorships')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    is_retired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRetired')
    sponsorships = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipConnection'), graphql_name='sponsorships', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=False)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )


class SponsorsTierConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorsTierEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SponsorsTier'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorsTierEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SponsorsTier', graphql_name='node')


class SponsorshipConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count', 'total_recurring_monthly_price_in_cents', 'total_recurring_monthly_price_in_dollars')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorshipEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Sponsorship'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_recurring_monthly_price_in_cents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRecurringMonthlyPriceInCents')
    total_recurring_monthly_price_in_dollars = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRecurringMonthlyPriceInDollars')


class SponsorshipEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Sponsorship', graphql_name='node')


class SponsorshipNewsletterConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorshipNewsletterEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SponsorshipNewsletter'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorshipNewsletterEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SponsorshipNewsletter', graphql_name='node')


class StargazerConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('StargazerEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StargazerEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'starred_at')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    starred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starredAt')


class StarredRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'is_over_limit', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('StarredRepositoryEdge'), graphql_name='edges')
    is_over_limit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOverLimit')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StarredRepositoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'starred_at')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')
    starred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starredAt')


class StartOrganizationMigrationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'org_migration')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    org_migration = sgqlc.types.Field('OrganizationMigration', graphql_name='orgMigration')


class StartRepositoryMigrationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository_migration')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_migration = sgqlc.types.Field('RepositoryMigration', graphql_name='repositoryMigration')


class StatusCheckConfiguration(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('context', 'integration_id')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')
    integration_id = sgqlc.types.Field(Int, graphql_name='integrationId')


class StatusCheckRollupContextConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('check_run_count', 'check_run_counts_by_state', 'edges', 'nodes', 'page_info', 'status_context_count', 'status_context_counts_by_state', 'total_count')
    check_run_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='checkRunCount')
    check_run_counts_by_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CheckRunStateCount)), graphql_name='checkRunCountsByState')
    edges = sgqlc.types.Field(sgqlc.types.list_of('StatusCheckRollupContextEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('StatusCheckRollupContext'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    status_context_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='statusContextCount')
    status_context_counts_by_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StatusContextStateCount')), graphql_name='statusContextCountsByState')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StatusCheckRollupContextEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('StatusCheckRollupContext', graphql_name='node')


class StatusContextStateCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('count', 'state')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')


class StripeConnectAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('account_id', 'billing_country_or_region', 'country_or_region', 'is_active', 'sponsors_listing', 'stripe_dashboard_url')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountId')
    billing_country_or_region = sgqlc.types.Field(String, graphql_name='billingCountryOrRegion')
    country_or_region = sgqlc.types.Field(String, graphql_name='countryOrRegion')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    sponsors_listing = sgqlc.types.Field(sgqlc.types.non_null('SponsorsListing'), graphql_name='sponsorsListing')
    stripe_dashboard_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='stripeDashboardUrl')


class SubIssuesSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('completed', 'percent_completed', 'total')
    completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='completed')
    percent_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='percentCompleted')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class SubmitPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class Submodule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('branch', 'git_url', 'name', 'name_raw', 'path', 'path_raw', 'subproject_commit_oid')
    branch = sgqlc.types.Field(String, graphql_name='branch')
    git_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='gitUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_raw = sgqlc.types.Field(sgqlc.types.non_null(Base64String), graphql_name='nameRaw')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    path_raw = sgqlc.types.Field(sgqlc.types.non_null(Base64String), graphql_name='pathRaw')
    subproject_commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='subprojectCommitOid')


class SubmoduleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SubmoduleEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(Submodule), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SubmoduleEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(Submodule, graphql_name='node')


class SuggestedReviewer(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('is_author', 'is_commenter', 'reviewer')
    is_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAuthor')
    is_commenter = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCommenter')
    reviewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='reviewer')


class TagNamePatternParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'negate', 'operator', 'pattern')
    name = sgqlc.types.Field(String, graphql_name='name')
    negate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='negate')
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operator')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')


class TeamConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamDiscussionCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussionCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussionComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamDiscussionCommentEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('TeamDiscussionComment', graphql_name='node')


class TeamDiscussionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussion'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamDiscussionEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('TeamDiscussion', graphql_name='node')


class TeamEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Team', graphql_name='node')


class TeamMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamMemberEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'member_access_resource_path', 'member_access_url', 'node', 'role')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    member_access_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='memberAccessResourcePath')
    member_access_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='memberAccessUrl')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberRole), graphql_name='role')


class TeamRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamRepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamRepositoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node', 'permission')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')


class TextMatch(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('fragment', 'highlights', 'property')
    fragment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fragment')
    highlights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TextMatchHighlight'))), graphql_name='highlights')
    property = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='property')


class TextMatchHighlight(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('begin_indice', 'end_indice', 'text')
    begin_indice = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='beginIndice')
    end_indice = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endIndice')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')


class TransferEnterpriseOrganizationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class TransferIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class TreeEntry(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('extension', 'is_generated', 'language', 'line_count', 'mode', 'name', 'name_raw', 'object', 'oid', 'path', 'path_raw', 'repository', 'size', 'submodule', 'type')
    extension = sgqlc.types.Field(String, graphql_name='extension')
    is_generated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGenerated')
    language = sgqlc.types.Field('Language', graphql_name='language')
    line_count = sgqlc.types.Field(Int, graphql_name='lineCount')
    mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mode')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_raw = sgqlc.types.Field(sgqlc.types.non_null(Base64String), graphql_name='nameRaw')
    object = sgqlc.types.Field(GitObject, graphql_name='object')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    path = sgqlc.types.Field(String, graphql_name='path')
    path_raw = sgqlc.types.Field(Base64String, graphql_name='pathRaw')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    submodule = sgqlc.types.Field(Submodule, graphql_name='submodule')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class UnarchiveProjectV2ItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item = sgqlc.types.Field('ProjectV2Item', graphql_name='item')


class UnarchiveRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UnfollowOrganizationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class UnfollowUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class UnlinkProjectV2FromRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UnlinkProjectV2FromTeamPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'team')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team = sgqlc.types.Field('Team', graphql_name='team')


class UnlinkRepositoryFromProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UnlockLockablePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'unlocked_record')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    unlocked_record = sgqlc.types.Field(Lockable, graphql_name='unlockedRecord')


class UnmarkDiscussionCommentAsAnswerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class UnmarkFileAsViewedPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class UnmarkIssueAsDuplicatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'duplicate')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    duplicate = sgqlc.types.Field('IssueOrPullRequest', graphql_name='duplicate')


class UnmarkProjectV2AsTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class UnminimizeCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'unminimized_comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    unminimized_comment = sgqlc.types.Field(Minimizable, graphql_name='unminimizedComment')


class UnpinIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(ID, graphql_name='id')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class UnresolveReviewThreadPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'thread')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread = sgqlc.types.Field('PullRequestReviewThread', graphql_name='thread')


class UpdateBranchProtectionRulePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('branch_protection_rule', 'client_mutation_id')
    branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='branchProtectionRule')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateCheckRunPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('check_run', 'client_mutation_id')
    check_run = sgqlc.types.Field('CheckRun', graphql_name='checkRun')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateCheckSuitePreferencesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UpdateDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('DiscussionComment', graphql_name='comment')


class UpdateDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class UpdateEnterpriseAdministratorRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseDefaultRepositoryPermissionSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseDeployKeySettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanDeleteIssuesSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanMakePurchasesSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseOrganizationProjectsSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseOwnerOrganizationRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseProfilePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')


class UpdateEnterpriseRepositoryProjectsSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseTeamDiscussionsSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseTwoFactorAuthenticationDisallowedMethodsSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'enterprise', 'message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnvironmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'environment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    environment = sgqlc.types.Field('Environment', graphql_name='environment')


class UpdateIpAllowListEnabledSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field('IpAllowListOwner', graphql_name='owner')


class UpdateIpAllowListEntryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ip_allow_list_entry')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ip_allow_list_entry = sgqlc.types.Field('IpAllowListEntry', graphql_name='ipAllowListEntry')


class UpdateIpAllowListForInstalledAppsEnabledSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field('IpAllowListOwner', graphql_name='owner')


class UpdateIssueCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_comment = sgqlc.types.Field('IssueComment', graphql_name='issueComment')


class UpdateIssueIssueTypePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class UpdateIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'issue')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class UpdateIssueTypePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'issue_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_type = sgqlc.types.Field('IssueType', graphql_name='issueType')


class UpdateLabelPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'label')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    label = sgqlc.types.Field('Label', graphql_name='label')


class UpdateNotificationRestrictionSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'owner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field('VerifiableDomainOwner', graphql_name='owner')


class UpdateOrganizationAllowPrivateRepositoryForkingSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class UpdateOrganizationWebCommitSignoffSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message', 'organization')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class UpdateParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('update_allows_fetch_and_merge',)
    update_allows_fetch_and_merge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAllowsFetchAndMerge')


class UpdatePatreonSponsorabilityPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsors_listing')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsors_listing = sgqlc.types.Field('SponsorsListing', graphql_name='sponsorsListing')


class UpdateProjectCardPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_card')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card = sgqlc.types.Field('ProjectCard', graphql_name='projectCard')


class UpdateProjectColumnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_column')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column = sgqlc.types.Field('ProjectColumn', graphql_name='projectColumn')


class UpdateProjectPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class UpdateProjectV2CollaboratorsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'collaborators')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    collaborators = sgqlc.types.Field(ProjectV2ActorConnection, graphql_name='collaborators', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class UpdateProjectV2DraftIssuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'draft_issue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    draft_issue = sgqlc.types.Field('DraftIssue', graphql_name='draftIssue')


class UpdateProjectV2FieldPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2_field')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2_field = sgqlc.types.Field('ProjectV2FieldConfiguration', graphql_name='projectV2Field')


class UpdateProjectV2ItemFieldValuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2_item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2_item = sgqlc.types.Field('ProjectV2Item', graphql_name='projectV2Item')


class UpdateProjectV2ItemPositionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'items')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    items = sgqlc.types.Field(ProjectV2ItemConnection, graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class UpdateProjectV2Payload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'project_v2')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_v2 = sgqlc.types.Field('ProjectV2', graphql_name='projectV2')


class UpdateProjectV2StatusUpdatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'status_update')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    status_update = sgqlc.types.Field('ProjectV2StatusUpdate', graphql_name='statusUpdate')


class UpdatePullRequestBranchPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class UpdatePullRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('actor', 'client_mutation_id', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class UpdatePullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review_comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_comment = sgqlc.types.Field('PullRequestReviewComment', graphql_name='pullRequestReviewComment')


class UpdatePullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'pull_request_review')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class UpdateRefPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ref')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class UpdateRefsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UpdateRepositoryRulesetPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ruleset')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ruleset = sgqlc.types.Field('RepositoryRuleset', graphql_name='ruleset')


class UpdateRepositoryWebCommitSignoffSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'message', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UpdateSponsorshipPreferencesPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'sponsorship')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    sponsorship = sgqlc.types.Field('Sponsorship', graphql_name='sponsorship')


class UpdateSubscriptionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subscribable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subscribable = sgqlc.types.Field(Subscribable, graphql_name='subscribable')


class UpdateTeamDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'team_discussion_comment')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_discussion_comment = sgqlc.types.Field('TeamDiscussionComment', graphql_name='teamDiscussionComment')


class UpdateTeamDiscussionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'team_discussion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_discussion = sgqlc.types.Field('TeamDiscussion', graphql_name='teamDiscussion')


class UpdateTeamReviewAssignmentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'team')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team = sgqlc.types.Field('Team', graphql_name='team')


class UpdateTeamsRepositoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'repository', 'teams')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    teams = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Team')), graphql_name='teams')


class UpdateTopicsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invalid_topic_names', 'repository')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invalid_topic_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='invalidTopicNames')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UpdateUserListPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'list')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    list = sgqlc.types.Field('UserList', graphql_name='list')


class UpdateUserListsForItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'item', 'lists', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    item = sgqlc.types.Field('UserListItems', graphql_name='item')
    lists = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserList')), graphql_name='lists')
    user = sgqlc.types.Field('User', graphql_name='user')


class UserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserContentEditConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserContentEditEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserContentEdit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserContentEditEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserContentEdit', graphql_name='node')


class UserEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')


class UserEmailMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('primary', 'type', 'value')
    primary = sgqlc.types.Field(Boolean, graphql_name='primary')
    type = sgqlc.types.Field(String, graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class UserListConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserListEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserList'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserListEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserList', graphql_name='node')


class UserListItemsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserListItemsEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserListItems'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserListItemsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserListItems', graphql_name='node')


class UserListSuggestion(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UserNamespaceRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserNamespaceRepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserNamespaceRepository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserNamespaceRepositoryEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserNamespaceRepository', graphql_name='node')


class UserStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserStatusEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserStatus'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserStatusEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserStatus', graphql_name='node')


class VerifiableDomainConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('VerifiableDomainEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('VerifiableDomain'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class VerifiableDomainEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('VerifiableDomain', graphql_name='node')


class VerifyVerifiableDomainPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'domain')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    domain = sgqlc.types.Field('VerifiableDomain', graphql_name='domain')


class WorkflowFileReference(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('path', 'ref', 'repository_id', 'sha')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    ref = sgqlc.types.Field(String, graphql_name='ref')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryId')
    sha = sgqlc.types.Field(String, graphql_name='sha')


class WorkflowRunConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.list_of('WorkflowRunEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('WorkflowRun'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkflowRunEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('WorkflowRun', graphql_name='node')


class WorkflowsParameters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('do_not_enforce_on_create', 'workflows')
    do_not_enforce_on_create = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doNotEnforceOnCreate')
    workflows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkflowFileReference))), graphql_name='workflows')


class AddedToMergeQueueEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'enqueuer', 'merge_queue', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enqueuer = sgqlc.types.Field('User', graphql_name='enqueuer')
    merge_queue = sgqlc.types.Field('MergeQueue', graphql_name='mergeQueue')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class AddedToProjectEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class AddedToProjectV2Event(sgqlc.types.Type, Node, ProjectV2Event):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class App(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('client_id', 'created_at', 'database_id', 'description', 'ip_allow_list_entries', 'logo_background_color', 'logo_url', 'name', 'slug', 'updated_at', 'url')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    ip_allow_list_entries = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListEntryConnection), graphql_name='ipAllowListEntries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(IpAllowListEntryOrder, graphql_name='orderBy', default={'field': 'ALLOW_LIST_VALUE', 'direction': 'ASC'})),
))
    )
    logo_background_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoBackgroundColor')
    logo_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='logoUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class AssignedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'assignable', 'assignee', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    assignable = sgqlc.types.Field(sgqlc.types.non_null(Assignable), graphql_name='assignable')
    assignee = sgqlc.types.Field('Assignee', graphql_name='assignee')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class AutoMergeDisabledEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'disabler', 'pull_request', 'reason', 'reason_code')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    disabler = sgqlc.types.Field('User', graphql_name='disabler')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    reason_code = sgqlc.types.Field(String, graphql_name='reasonCode')


class AutoMergeEnabledEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'enabler', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enabler = sgqlc.types.Field('User', graphql_name='enabler')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class AutoRebaseEnabledEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'enabler', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enabler = sgqlc.types.Field('User', graphql_name='enabler')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class AutoSquashEnabledEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'enabler', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enabler = sgqlc.types.Field('User', graphql_name='enabler')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class AutomaticBaseChangeFailedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'new_base', 'old_base', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    new_base = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newBase')
    old_base = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oldBase')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class AutomaticBaseChangeSucceededEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'new_base', 'old_base', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    new_base = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newBase')
    old_base = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oldBase')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class BaseRefChangedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'current_ref_name', 'database_id', 'previous_ref_name', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    current_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentRefName')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    previous_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='previousRefName')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class BaseRefDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'base_ref_name', 'created_at', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    base_ref_name = sgqlc.types.Field(String, graphql_name='baseRefName')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class BaseRefForcePushedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'after_commit', 'before_commit', 'created_at', 'pull_request', 'ref')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    after_commit = sgqlc.types.Field('Commit', graphql_name='afterCommit')
    before_commit = sgqlc.types.Field('Commit', graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class Blob(sgqlc.types.Type, GitObject, Node):
    __schema__ = schema
    __field_names__ = ('byte_size', 'is_binary', 'is_truncated', 'text')
    byte_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='byteSize')
    is_binary = sgqlc.types.Field(Boolean, graphql_name='isBinary')
    is_truncated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTruncated')
    text = sgqlc.types.Field(String, graphql_name='text')


class BlockedByAddedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'blocking_issue', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    blocking_issue = sgqlc.types.Field('Issue', graphql_name='blockingIssue')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class BlockedByRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'blocking_issue', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    blocking_issue = sgqlc.types.Field('Issue', graphql_name='blockingIssue')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class BlockingAddedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'blocked_issue', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    blocked_issue = sgqlc.types.Field('Issue', graphql_name='blockedIssue')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class BlockingRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'blocked_issue', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    blocked_issue = sgqlc.types.Field('Issue', graphql_name='blockedIssue')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class Bot(sgqlc.types.Type, Actor, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('created_at', 'database_id', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class BranchProtectionRule(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('allows_deletions', 'allows_force_pushes', 'blocks_creations', 'branch_protection_rule_conflicts', 'bypass_force_push_allowances', 'bypass_pull_request_allowances', 'creator', 'database_id', 'dismisses_stale_reviews', 'is_admin_enforced', 'lock_allows_fetch_and_merge', 'lock_branch', 'matching_refs', 'pattern', 'push_allowances', 'repository', 'require_last_push_approval', 'required_approving_review_count', 'required_deployment_environments', 'required_status_check_contexts', 'required_status_checks', 'requires_approving_reviews', 'requires_code_owner_reviews', 'requires_commit_signatures', 'requires_conversation_resolution', 'requires_deployments', 'requires_linear_history', 'requires_status_checks', 'requires_strict_status_checks', 'restricts_pushes', 'restricts_review_dismissals', 'review_dismissal_allowances')
    allows_deletions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowsDeletions')
    allows_force_pushes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowsForcePushes')
    blocks_creations = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='blocksCreations')
    branch_protection_rule_conflicts = sgqlc.types.Field(sgqlc.types.non_null(BranchProtectionRuleConflictConnection), graphql_name='branchProtectionRuleConflicts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    bypass_force_push_allowances = sgqlc.types.Field(sgqlc.types.non_null(BypassForcePushAllowanceConnection), graphql_name='bypassForcePushAllowances', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    bypass_pull_request_allowances = sgqlc.types.Field(sgqlc.types.non_null(BypassPullRequestAllowanceConnection), graphql_name='bypassPullRequestAllowances', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    dismisses_stale_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dismissesStaleReviews')
    is_admin_enforced = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminEnforced')
    lock_allows_fetch_and_merge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='lockAllowsFetchAndMerge')
    lock_branch = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='lockBranch')
    matching_refs = sgqlc.types.Field(sgqlc.types.non_null(RefConnection), graphql_name='matchingRefs', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')
    push_allowances = sgqlc.types.Field(sgqlc.types.non_null(PushAllowanceConnection), graphql_name='pushAllowances', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    require_last_push_approval = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requireLastPushApproval')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    required_deployment_environments = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='requiredDeploymentEnvironments')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='requiredStatusCheckContexts')
    required_status_checks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RequiredStatusCheckDescription)), graphql_name='requiredStatusChecks')
    requires_approving_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresApprovingReviews')
    requires_code_owner_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresCodeOwnerReviews')
    requires_commit_signatures = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresCommitSignatures')
    requires_conversation_resolution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresConversationResolution')
    requires_deployments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresDeployments')
    requires_linear_history = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresLinearHistory')
    requires_status_checks = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresStatusChecks')
    requires_strict_status_checks = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresStrictStatusChecks')
    restricts_pushes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restrictsPushes')
    restricts_review_dismissals = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restrictsReviewDismissals')
    review_dismissal_allowances = sgqlc.types.Field(sgqlc.types.non_null(ReviewDismissalAllowanceConnection), graphql_name='reviewDismissalAllowances', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class BypassForcePushAllowance(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'branch_protection_rule')
    actor = sgqlc.types.Field('BranchActorAllowanceActor', graphql_name='actor')
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')


class BypassPullRequestAllowance(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'branch_protection_rule')
    actor = sgqlc.types.Field('BranchActorAllowanceActor', graphql_name='actor')
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')


class CWE(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('cwe_id', 'description', 'name')
    cwe_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cweId')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CheckRun(sgqlc.types.Type, Node, RequirableByPullRequest, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('annotations', 'check_suite', 'completed_at', 'conclusion', 'database_id', 'deployment', 'details_url', 'external_id', 'name', 'pending_deployment_request', 'permalink', 'repository', 'started_at', 'status', 'steps', 'summary', 'text', 'title')
    annotations = sgqlc.types.Field(CheckAnnotationConnection, graphql_name='annotations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    check_suite = sgqlc.types.Field(sgqlc.types.non_null('CheckSuite'), graphql_name='checkSuite')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    conclusion = sgqlc.types.Field(CheckConclusionState, graphql_name='conclusion')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    deployment = sgqlc.types.Field('Deployment', graphql_name='deployment')
    details_url = sgqlc.types.Field(URI, graphql_name='detailsUrl')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pending_deployment_request = sgqlc.types.Field(DeploymentRequest, graphql_name='pendingDeploymentRequest')
    permalink = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='permalink')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(CheckStatusState), graphql_name='status')
    steps = sgqlc.types.Field(CheckStepConnection, graphql_name='steps', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('number', sgqlc.types.Arg(Int, graphql_name='number', default=None)),
))
    )
    summary = sgqlc.types.Field(String, graphql_name='summary')
    text = sgqlc.types.Field(String, graphql_name='text')
    title = sgqlc.types.Field(String, graphql_name='title')


class CheckSuite(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('app', 'branch', 'check_runs', 'commit', 'conclusion', 'created_at', 'creator', 'database_id', 'matching_pull_requests', 'push', 'repository', 'resource_path', 'status', 'updated_at', 'url', 'workflow_run')
    app = sgqlc.types.Field(App, graphql_name='app')
    branch = sgqlc.types.Field('Ref', graphql_name='branch')
    check_runs = sgqlc.types.Field(CheckRunConnection, graphql_name='checkRuns', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter_by', sgqlc.types.Arg(CheckRunFilter, graphql_name='filterBy', default=None)),
))
    )
    commit = sgqlc.types.Field(sgqlc.types.non_null('Commit'), graphql_name='commit')
    conclusion = sgqlc.types.Field(CheckConclusionState, graphql_name='conclusion')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field('User', graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    matching_pull_requests = sgqlc.types.Field(PullRequestConnection, graphql_name='matchingPullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    push = sgqlc.types.Field('Push', graphql_name='push')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    status = sgqlc.types.Field(sgqlc.types.non_null(CheckStatusState), graphql_name='status')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    workflow_run = sgqlc.types.Field('WorkflowRun', graphql_name='workflowRun')


class ClosedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('actor', 'closable', 'closer', 'created_at', 'duplicate_of', 'state_reason')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    closable = sgqlc.types.Field(sgqlc.types.non_null(Closable), graphql_name='closable')
    closer = sgqlc.types.Field('Closer', graphql_name='closer')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    duplicate_of = sgqlc.types.Field('IssueOrPullRequest', graphql_name='duplicateOf')
    state_reason = sgqlc.types.Field(IssueStateReason, graphql_name='stateReason')


class CodeOfConduct(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('body', 'key', 'name', 'resource_path', 'url')
    body = sgqlc.types.Field(String, graphql_name='body')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    resource_path = sgqlc.types.Field(URI, graphql_name='resourcePath')
    url = sgqlc.types.Field(URI, graphql_name='url')


class CommentDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'database_id', 'deleted_comment_author')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    deleted_comment_author = sgqlc.types.Field(Actor, graphql_name='deletedCommentAuthor')


class Commit(sgqlc.types.Type, GitObject, Node, Subscribable, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('additions', 'associated_pull_requests', 'author', 'authored_by_committer', 'authored_date', 'authors', 'blame', 'changed_files_if_available', 'check_suites', 'comments', 'committed_date', 'committed_via_web', 'committer', 'deletions', 'deployments', 'file', 'history', 'message', 'message_body', 'message_body_html', 'message_headline', 'message_headline_html', 'on_behalf_of', 'parents', 'signature', 'status', 'status_check_rollup', 'submodules', 'tarball_url', 'tree', 'tree_resource_path', 'tree_url', 'zipball_url')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    associated_pull_requests = sgqlc.types.Field(PullRequestConnection, graphql_name='associatedPullRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(PullRequestOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )
    author = sgqlc.types.Field(GitActor, graphql_name='author')
    authored_by_committer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='authoredByCommitter')
    authored_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='authoredDate')
    authors = sgqlc.types.Field(sgqlc.types.non_null(GitActorConnection), graphql_name='authors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    blame = sgqlc.types.Field(sgqlc.types.non_null(Blame), graphql_name='blame', args=sgqlc.types.ArgDict((
        ('path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='path', default=None)),
))
    )
    changed_files_if_available = sgqlc.types.Field(Int, graphql_name='changedFilesIfAvailable')
    check_suites = sgqlc.types.Field(CheckSuiteConnection, graphql_name='checkSuites', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter_by', sgqlc.types.Arg(CheckSuiteFilter, graphql_name='filterBy', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    committed_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='committedDate')
    committed_via_web = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='committedViaWeb')
    committer = sgqlc.types.Field(GitActor, graphql_name='committer')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    deployments = sgqlc.types.Field(DeploymentConnection, graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('environments', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='environments', default=None)),
        ('order_by', sgqlc.types.Arg(DeploymentOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    file = sgqlc.types.Field(TreeEntry, graphql_name='file', args=sgqlc.types.ArgDict((
        ('path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='path', default=None)),
))
    )
    history = sgqlc.types.Field(sgqlc.types.non_null(CommitHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('path', sgqlc.types.Arg(String, graphql_name='path', default=None)),
        ('author', sgqlc.types.Arg(CommitAuthor, graphql_name='author', default=None)),
        ('since', sgqlc.types.Arg(GitTimestamp, graphql_name='since', default=None)),
        ('until', sgqlc.types.Arg(GitTimestamp, graphql_name='until', default=None)),
))
    )
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    message_body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='messageBody')
    message_body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageBodyHTML')
    message_headline = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='messageHeadline')
    message_headline_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageHeadlineHTML')
    on_behalf_of = sgqlc.types.Field('Organization', graphql_name='onBehalfOf')
    parents = sgqlc.types.Field(sgqlc.types.non_null(CommitConnection), graphql_name='parents', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    signature = sgqlc.types.Field(GitSignature, graphql_name='signature')
    status = sgqlc.types.Field('Status', graphql_name='status')
    status_check_rollup = sgqlc.types.Field('StatusCheckRollup', graphql_name='statusCheckRollup')
    submodules = sgqlc.types.Field(sgqlc.types.non_null(SubmoduleConnection), graphql_name='submodules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    tarball_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='tarballUrl')
    tree = sgqlc.types.Field(sgqlc.types.non_null('Tree'), graphql_name='tree')
    tree_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='treeResourcePath')
    tree_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='treeUrl')
    zipball_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='zipballUrl')


class CommitComment(sgqlc.types.Type, Comment, Deletable, Minimizable, Node, Reactable, RepositoryNode, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('commit', 'path', 'position', 'resource_path', 'url')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class CommitCommentThread(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = schema
    __field_names__ = ('comments', 'commit', 'path', 'position')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')


class Comparison(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('ahead_by', 'base_target', 'behind_by', 'commits', 'head_target', 'status')
    ahead_by = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='aheadBy')
    base_target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='baseTarget')
    behind_by = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='behindBy')
    commits = sgqlc.types.Field(sgqlc.types.non_null(ComparisonCommitConnection), graphql_name='commits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    head_target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='headTarget')
    status = sgqlc.types.Field(sgqlc.types.non_null(ComparisonStatus), graphql_name='status')


class ConnectedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'is_cross_repository', 'source', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    source = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='source')
    subject = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='subject')


class ConvertToDraftEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class ConvertedFromDraftEvent(sgqlc.types.Type, Node, ProjectV2Event):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class ConvertedNoteToIssueEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'database_id', 'project_column_name')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    project_column_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectColumnName')


class ConvertedToDiscussionEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'discussion')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    discussion = sgqlc.types.Field('Discussion', graphql_name='discussion')


class CreatedCommitContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ('commit_count', 'repository')
    commit_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='commitCount')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class CreatedIssueContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ('issue',)
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')


class CreatedPullRequestContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ('pull_request',)
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class CreatedPullRequestReviewContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ('pull_request', 'pull_request_review', 'repository')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class CreatedRepositoryContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ('repository',)
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class CrossReferencedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'is_cross_repository', 'referenced_at', 'source', 'target', 'will_close_target')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    referenced_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='referencedAt')
    source = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='source')
    target = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='target')
    will_close_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='willCloseTarget')


class DemilestonedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'milestone_title', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    milestone_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='milestoneTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('MilestoneItem'), graphql_name='subject')


class DependabotUpdate(sgqlc.types.Type, RepositoryNode):
    __schema__ = schema
    __field_names__ = ('error', 'pull_request')
    error = sgqlc.types.Field(DependabotUpdateError, graphql_name='error')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class DependencyGraphManifest(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('blob_path', 'dependencies', 'dependencies_count', 'exceeds_max_size', 'filename', 'parseable', 'repository')
    blob_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='blobPath')
    dependencies = sgqlc.types.Field(DependencyGraphDependencyConnection, graphql_name='dependencies', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    dependencies_count = sgqlc.types.Field(Int, graphql_name='dependenciesCount')
    exceeds_max_size = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exceedsMaxSize')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    parseable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='parseable')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class DeployKey(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'enabled', 'key', 'read_only', 'title', 'verified')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    read_only = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readOnly')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verified')


class DeployedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'database_id', 'deployment', 'pull_request', 'ref')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    deployment = sgqlc.types.Field(sgqlc.types.non_null('Deployment'), graphql_name='deployment')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class Deployment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('commit', 'commit_oid', 'created_at', 'creator', 'database_id', 'description', 'environment', 'latest_environment', 'latest_status', 'original_environment', 'payload', 'ref', 'repository', 'state', 'statuses', 'task', 'updated_at')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    commit_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='commitOid')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(sgqlc.types.non_null(Actor), graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    latest_environment = sgqlc.types.Field(String, graphql_name='latestEnvironment')
    latest_status = sgqlc.types.Field('DeploymentStatus', graphql_name='latestStatus')
    original_environment = sgqlc.types.Field(String, graphql_name='originalEnvironment')
    payload = sgqlc.types.Field(String, graphql_name='payload')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    state = sgqlc.types.Field(DeploymentState, graphql_name='state')
    statuses = sgqlc.types.Field(DeploymentStatusConnection, graphql_name='statuses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    task = sgqlc.types.Field(String, graphql_name='task')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class DeploymentEnvironmentChangedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'deployment_status', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    deployment_status = sgqlc.types.Field(sgqlc.types.non_null('DeploymentStatus'), graphql_name='deploymentStatus')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class DeploymentReview(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('comment', 'database_id', 'environments', 'state', 'user')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    environments = sgqlc.types.Field(sgqlc.types.non_null(EnvironmentConnection), graphql_name='environments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(DeploymentReviewState), graphql_name='state')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class DeploymentStatus(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'creator', 'deployment', 'description', 'environment', 'environment_url', 'log_url', 'state', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(sgqlc.types.non_null(Actor), graphql_name='creator')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(Deployment), graphql_name='deployment')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    environment_url = sgqlc.types.Field(URI, graphql_name='environmentUrl')
    log_url = sgqlc.types.Field(URI, graphql_name='logUrl')
    state = sgqlc.types.Field(sgqlc.types.non_null(DeploymentStatusState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class DisconnectedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'is_cross_repository', 'source', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    source = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='source')
    subject = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='subject')


class Discussion(sgqlc.types.Type, Closable, Comment, Deletable, Labelable, Lockable, Node, Reactable, RepositoryNode, Subscribable, Updatable, Votable):
    __schema__ = schema
    __field_names__ = ('answer', 'answer_chosen_at', 'answer_chosen_by', 'category', 'comments', 'is_answered', 'number', 'poll', 'resource_path', 'state_reason', 'title', 'url')
    answer = sgqlc.types.Field('DiscussionComment', graphql_name='answer')
    answer_chosen_at = sgqlc.types.Field(DateTime, graphql_name='answerChosenAt')
    answer_chosen_by = sgqlc.types.Field(Actor, graphql_name='answerChosenBy')
    category = sgqlc.types.Field(sgqlc.types.non_null('DiscussionCategory'), graphql_name='category')
    comments = sgqlc.types.Field(sgqlc.types.non_null(DiscussionCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    is_answered = sgqlc.types.Field(Boolean, graphql_name='isAnswered')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    poll = sgqlc.types.Field('DiscussionPoll', graphql_name='poll')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state_reason = sgqlc.types.Field(DiscussionStateReason, graphql_name='stateReason')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class DiscussionCategory(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = schema
    __field_names__ = ('created_at', 'description', 'emoji', 'emoji_html', 'is_answerable', 'name', 'slug', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    emoji = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='emoji')
    emoji_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='emojiHTML')
    is_answerable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAnswerable')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class DiscussionComment(sgqlc.types.Type, Comment, Deletable, Minimizable, Node, Reactable, Updatable, UpdatableComment, Votable):
    __schema__ = schema
    __field_names__ = ('deleted_at', 'discussion', 'is_answer', 'replies', 'reply_to', 'resource_path', 'url', 'viewer_can_mark_as_answer', 'viewer_can_unmark_as_answer')
    deleted_at = sgqlc.types.Field(DateTime, graphql_name='deletedAt')
    discussion = sgqlc.types.Field(Discussion, graphql_name='discussion')
    is_answer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAnswer')
    replies = sgqlc.types.Field(sgqlc.types.non_null(DiscussionCommentConnection), graphql_name='replies', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    reply_to = sgqlc.types.Field('DiscussionComment', graphql_name='replyTo')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_mark_as_answer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMarkAsAnswer')
    viewer_can_unmark_as_answer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUnmarkAsAnswer')


class DiscussionPoll(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('discussion', 'options', 'question', 'total_vote_count', 'viewer_can_vote', 'viewer_has_voted')
    discussion = sgqlc.types.Field(Discussion, graphql_name='discussion')
    options = sgqlc.types.Field(DiscussionPollOptionConnection, graphql_name='options', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(DiscussionPollOptionOrder, graphql_name='orderBy', default={'field': 'AUTHORED_ORDER', 'direction': 'ASC'})),
))
    )
    question = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='question')
    total_vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalVoteCount')
    viewer_can_vote = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanVote')
    viewer_has_voted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasVoted')


class DiscussionPollOption(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('option', 'poll', 'total_vote_count', 'viewer_has_voted')
    option = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='option')
    poll = sgqlc.types.Field(DiscussionPoll, graphql_name='poll')
    total_vote_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalVoteCount')
    viewer_has_voted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasVoted')


class DraftIssue(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('assignees', 'body', 'body_html', 'body_text', 'created_at', 'creator', 'project_v2_items', 'projects_v2', 'title', 'updated_at')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    project_v2_items = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemConnection), graphql_name='projectV2Items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_v2 = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2Connection), graphql_name='projectsV2', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Enterprise(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('announcement_banner', 'avatar_url', 'billing_email', 'billing_info', 'created_at', 'database_id', 'description', 'description_html', 'location', 'members', 'name', 'organizations', 'owner_info', 'readme', 'readme_html', 'resource_path', 'ruleset', 'rulesets', 'security_contact_email', 'slug', 'updated_at', 'url', 'user_namespace_repositories', 'viewer_is_admin', 'website_url')
    announcement_banner = sgqlc.types.Field(AnnouncementBanner, graphql_name='announcementBanner')
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    billing_email = sgqlc.types.Field(String, graphql_name='billingEmail')
    billing_info = sgqlc.types.Field(EnterpriseBillingInfo, graphql_name='billingInfo')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    location = sgqlc.types.Field(String, graphql_name='location')
    members = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('organization_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='organizationLogins', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('role', sgqlc.types.Arg(EnterpriseUserAccountMembershipRole, graphql_name='role', default=None)),
        ('deployment', sgqlc.types.Arg(EnterpriseUserDeployment, graphql_name='deployment', default=None)),
        ('has_two_factor_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasTwoFactorEnabled', default=None)),
        ('two_factor_method_security', sgqlc.types.Arg(TwoFactorCredentialSecurityType, graphql_name='twoFactorMethodSecurity', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('viewer_organization_role', sgqlc.types.Arg(RoleInOrganization, graphql_name='viewerOrganizationRole', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    owner_info = sgqlc.types.Field(EnterpriseOwnerInfo, graphql_name='ownerInfo')
    readme = sgqlc.types.Field(String, graphql_name='readme')
    readme_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='readmeHTML')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    ruleset = sgqlc.types.Field('RepositoryRuleset', graphql_name='ruleset', args=sgqlc.types.ArgDict((
        ('database_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='databaseId', default=None)),
))
    )
    rulesets = sgqlc.types.Field(RepositoryRulesetConnection, graphql_name='rulesets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    security_contact_email = sgqlc.types.Field(String, graphql_name='securityContactEmail')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_namespace_repositories = sgqlc.types.Field(sgqlc.types.non_null(UserNamespaceRepositoryConnection), graphql_name='userNamespaceRepositories', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsAdmin')
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class EnterpriseAdministratorInvitation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'email', 'enterprise', 'invitee', 'inviter', 'role')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    inviter = sgqlc.types.Field('User', graphql_name='inviter')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role')


class EnterpriseIdentityProvider(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('digest_method', 'enterprise', 'external_identities', 'idp_certificate', 'issuer', 'recovery_codes', 'signature_method', 'sso_url')
    digest_method = sgqlc.types.Field(SamlDigestAlgorithm, graphql_name='digestMethod')
    enterprise = sgqlc.types.Field(Enterprise, graphql_name='enterprise')
    external_identities = sgqlc.types.Field(sgqlc.types.non_null(ExternalIdentityConnection), graphql_name='externalIdentities', args=sgqlc.types.ArgDict((
        ('members_only', sgqlc.types.Arg(Boolean, graphql_name='membersOnly', default=None)),
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('user_name', sgqlc.types.Arg(String, graphql_name='userName', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    idp_certificate = sgqlc.types.Field(X509Certificate, graphql_name='idpCertificate')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    recovery_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='recoveryCodes')
    signature_method = sgqlc.types.Field(SamlSignatureAlgorithm, graphql_name='signatureMethod')
    sso_url = sgqlc.types.Field(URI, graphql_name='ssoUrl')


class EnterpriseMemberInvitation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'email', 'enterprise', 'invitee', 'inviter')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    inviter = sgqlc.types.Field('User', graphql_name='inviter')


class EnterpriseRepositoryInfo(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('is_private', 'name', 'name_with_owner')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')


class EnterpriseServerInstallation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'customer_name', 'host_name', 'is_connected', 'updated_at', 'user_accounts', 'user_accounts_uploads')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customerName')
    host_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hostName')
    is_connected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isConnected')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_accounts = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountConnection), graphql_name='userAccounts', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseServerUserAccountOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    user_accounts_uploads = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountsUploadConnection), graphql_name='userAccountsUploads', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseServerUserAccountsUploadOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class EnterpriseServerUserAccount(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'emails', 'enterprise_server_installation', 'is_site_admin', 'login', 'profile_name', 'remote_created_at', 'remote_user_id', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    emails = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountEmailConnection), graphql_name='emails', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseServerUserAccountEmailOrder, graphql_name='orderBy', default={'field': 'EMAIL', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    enterprise_server_installation = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallation), graphql_name='enterpriseServerInstallation')
    is_site_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSiteAdmin')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    profile_name = sgqlc.types.Field(String, graphql_name='profileName')
    remote_created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='remoteCreatedAt')
    remote_user_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='remoteUserId')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class EnterpriseServerUserAccountEmail(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'email', 'is_primary', 'updated_at', 'user_account')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrimary')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_account = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccount), graphql_name='userAccount')


class EnterpriseServerUserAccountsUpload(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'enterprise', 'enterprise_server_installation', 'name', 'sync_state', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    enterprise_server_installation = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallation), graphql_name='enterpriseServerInstallation')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    sync_state = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountsUploadSyncState), graphql_name='syncState')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class EnterpriseUserAccount(sgqlc.types.Type, Actor, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'enterprise', 'enterprise_installations', 'name', 'organizations', 'updated_at', 'user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    enterprise_installations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallationMembershipConnection), graphql_name='enterpriseInstallations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseServerInstallationOrder, graphql_name='orderBy', default={'field': 'HOST_NAME', 'direction': 'ASC'})),
        ('role', sgqlc.types.Arg(EnterpriseUserAccountMembershipRole, graphql_name='role', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseOrganizationMembershipConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('role', sgqlc.types.Arg(EnterpriseUserAccountMembershipRole, graphql_name='role', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user = sgqlc.types.Field('User', graphql_name='user')


class Environment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('database_id', 'is_pinned', 'latest_completed_deployment', 'name', 'pinned_position', 'protection_rules')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    is_pinned = sgqlc.types.Field(Boolean, graphql_name='isPinned')
    latest_completed_deployment = sgqlc.types.Field(Deployment, graphql_name='latestCompletedDeployment')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pinned_position = sgqlc.types.Field(Int, graphql_name='pinnedPosition')
    protection_rules = sgqlc.types.Field(sgqlc.types.non_null(DeploymentProtectionRuleConnection), graphql_name='protectionRules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ExternalIdentity(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('guid', 'organization_invitation', 'saml_identity', 'scim_identity', 'user')
    guid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='guid')
    organization_invitation = sgqlc.types.Field('OrganizationInvitation', graphql_name='organizationInvitation')
    saml_identity = sgqlc.types.Field(ExternalIdentitySamlAttributes, graphql_name='samlIdentity')
    scim_identity = sgqlc.types.Field(ExternalIdentityScimAttributes, graphql_name='scimIdentity')
    user = sgqlc.types.Field('User', graphql_name='user')


class GenericHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = schema
    __field_names__ = ()


class Gist(sgqlc.types.Type, Node, Starrable, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('comments', 'created_at', 'description', 'files', 'forks', 'is_fork', 'is_public', 'name', 'owner', 'pushed_at', 'updated_at')
    comments = sgqlc.types.Field(sgqlc.types.non_null(GistCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    files = sgqlc.types.Field(sgqlc.types.list_of(GistFile), graphql_name='files', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
        ('oid', sgqlc.types.Arg(GitObjectID, graphql_name='oid', default=None)),
))
    )
    forks = sgqlc.types.Field(sgqlc.types.non_null(GistConnection), graphql_name='forks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(GistOrder, graphql_name='orderBy', default=None)),
))
    )
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner = sgqlc.types.Field(RepositoryOwner, graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class GistComment(sgqlc.types.Type, Comment, Deletable, Minimizable, Node, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('database_id', 'gist')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    gist = sgqlc.types.Field(sgqlc.types.non_null(Gist), graphql_name='gist')


class GpgSignature(sgqlc.types.Type, GitSignature):
    __schema__ = schema
    __field_names__ = ('key_id',)
    key_id = sgqlc.types.Field(String, graphql_name='keyId')


class HeadRefDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'head_ref', 'head_ref_name', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    head_ref = sgqlc.types.Field('Ref', graphql_name='headRef')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class HeadRefForcePushedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'after_commit', 'before_commit', 'created_at', 'pull_request', 'ref')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    after_commit = sgqlc.types.Field(Commit, graphql_name='afterCommit')
    before_commit = sgqlc.types.Field(Commit, graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class HeadRefRestoredEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class IpAllowListEntry(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('allow_list_value', 'created_at', 'is_active', 'name', 'owner', 'updated_at')
    allow_list_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='allowListValue')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(String, graphql_name='name')
    owner = sgqlc.types.Field(sgqlc.types.non_null('IpAllowListOwner'), graphql_name='owner')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Issue(sgqlc.types.Type, Assignable, Closable, Comment, Deletable, Labelable, Lockable, Node, ProjectV2Owner, Reactable, RepositoryNode, Subscribable, SubscribableThread, UniformResourceLocatable, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('blocked_by', 'blocking', 'body_resource_path', 'body_url', 'closed_by_pull_requests_references', 'comments', 'duplicate_of', 'full_database_id', 'hovercard', 'is_pinned', 'is_read_by_viewer', 'issue_dependencies_summary', 'issue_type', 'linked_branches', 'milestone', 'number', 'parent', 'participants', 'project_items', 'state', 'state_reason', 'sub_issues', 'sub_issues_summary', 'timeline_items', 'title', 'title_html', 'tracked_in_issues', 'tracked_issues', 'tracked_issues_count', 'viewer_can_set_fields')
    blocked_by = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='blockedBy', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueDependencyOrder, graphql_name='orderBy', default={'field': 'DEPENDENCY_ADDED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    blocking = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='blocking', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueDependencyOrder, graphql_name='orderBy', default={'field': 'DEPENDENCY_ADDED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    body_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='bodyResourcePath')
    body_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='bodyUrl')
    closed_by_pull_requests_references = sgqlc.types.Field(PullRequestConnection, graphql_name='closedByPullRequestsReferences', args=sgqlc.types.ArgDict((
        ('include_closed_prs', sgqlc.types.Arg(Boolean, graphql_name='includeClosedPrs', default=False)),
        ('order_by_state', sgqlc.types.Arg(Boolean, graphql_name='orderByState', default=False)),
        ('user_linked_only', sgqlc.types.Arg(Boolean, graphql_name='userLinkedOnly', default=False)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueCommentOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    duplicate_of = sgqlc.types.Field('Issue', graphql_name='duplicateOf')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    hovercard = sgqlc.types.Field(sgqlc.types.non_null(Hovercard), graphql_name='hovercard', args=sgqlc.types.ArgDict((
        ('include_notification_contexts', sgqlc.types.Arg(Boolean, graphql_name='includeNotificationContexts', default=True)),
))
    )
    is_pinned = sgqlc.types.Field(Boolean, graphql_name='isPinned')
    is_read_by_viewer = sgqlc.types.Field(Boolean, graphql_name='isReadByViewer')
    issue_dependencies_summary = sgqlc.types.Field(sgqlc.types.non_null(IssueDependenciesSummary), graphql_name='issueDependenciesSummary')
    issue_type = sgqlc.types.Field('IssueType', graphql_name='issueType')
    linked_branches = sgqlc.types.Field(sgqlc.types.non_null(LinkedBranchConnection), graphql_name='linkedBranches', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    parent = sgqlc.types.Field('Issue', graphql_name='parent')
    participants = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    project_items = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemConnection), graphql_name='projectItems', args=sgqlc.types.ArgDict((
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=True)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(IssueState), graphql_name='state')
    state_reason = sgqlc.types.Field(IssueStateReason, graphql_name='stateReason', args=sgqlc.types.ArgDict((
        ('enable_duplicate', sgqlc.types.Arg(Boolean, graphql_name='enableDuplicate', default=False)),
))
    )
    sub_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='subIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sub_issues_summary = sgqlc.types.Field(sgqlc.types.non_null(SubIssuesSummary), graphql_name='subIssuesSummary')
    timeline_items = sgqlc.types.Field(sgqlc.types.non_null(IssueTimelineItemsConnection), graphql_name='timelineItems', args=sgqlc.types.ArgDict((
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('item_types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueTimelineItemsItemType)), graphql_name='itemTypes', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    title_html = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='titleHTML')
    tracked_in_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='trackedInIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    tracked_issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='trackedIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    tracked_issues_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='trackedIssuesCount', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(TrackedIssueStates), graphql_name='states', default=None)),
))
    )
    viewer_can_set_fields = sgqlc.types.Field(Boolean, graphql_name='viewerCanSetFields')


class IssueComment(sgqlc.types.Type, Comment, Deletable, Minimizable, Node, Reactable, RepositoryNode, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('full_database_id', 'issue', 'pull_request', 'resource_path', 'url')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class IssueType(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('color', 'description', 'is_enabled', 'issues', 'name')
    color = sgqlc.types.Field(sgqlc.types.non_null(IssueTypeColor), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEnabled')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('repository_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='repositoryId', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IssueTypeAddedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'issue_type')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    issue_type = sgqlc.types.Field(IssueType, graphql_name='issueType')


class IssueTypeChangedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'issue_type', 'prev_issue_type')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    issue_type = sgqlc.types.Field(IssueType, graphql_name='issueType')
    prev_issue_type = sgqlc.types.Field(IssueType, graphql_name='prevIssueType')


class IssueTypeRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'issue_type')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    issue_type = sgqlc.types.Field(IssueType, graphql_name='issueType')


class JoinedGitHubContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ()


class Label(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('color', 'created_at', 'description', 'is_default', 'issues', 'name', 'pull_requests', 'repository', 'resource_path', 'updated_at', 'url')
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class LabeledEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'label', 'labelable')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    label = sgqlc.types.Field(sgqlc.types.non_null(Label), graphql_name='label')
    labelable = sgqlc.types.Field(sgqlc.types.non_null(Labelable), graphql_name='labelable')


class Language(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('color', 'name')
    color = sgqlc.types.Field(String, graphql_name='color')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class License(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('body', 'conditions', 'description', 'featured', 'hidden', 'implementation', 'key', 'limitations', 'name', 'nickname', 'permissions', 'pseudo_license', 'spdx_id', 'url')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(LicenseRule)), graphql_name='conditions')
    description = sgqlc.types.Field(String, graphql_name='description')
    featured = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='featured')
    hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hidden')
    implementation = sgqlc.types.Field(String, graphql_name='implementation')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    limitations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(LicenseRule)), graphql_name='limitations')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(LicenseRule)), graphql_name='permissions')
    pseudo_license = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pseudoLicense')
    spdx_id = sgqlc.types.Field(String, graphql_name='spdxId')
    url = sgqlc.types.Field(URI, graphql_name='url')


class LinkedBranch(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('ref',)
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class LockedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'lock_reason', 'lockable')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    lock_reason = sgqlc.types.Field(LockReason, graphql_name='lockReason')
    lockable = sgqlc.types.Field(sgqlc.types.non_null(Lockable), graphql_name='lockable')


class Mannequin(sgqlc.types.Type, Actor, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('claimant', 'created_at', 'database_id', 'email', 'name', 'updated_at')
    claimant = sgqlc.types.Field('User', graphql_name='claimant')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class MarkedAsDuplicateEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'canonical', 'created_at', 'duplicate', 'is_cross_repository')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    canonical = sgqlc.types.Field('IssueOrPullRequest', graphql_name='canonical')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    duplicate = sgqlc.types.Field('IssueOrPullRequest', graphql_name='duplicate')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')


class MarketplaceCategory(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('description', 'how_it_works', 'name', 'primary_listing_count', 'resource_path', 'secondary_listing_count', 'slug', 'url')
    description = sgqlc.types.Field(String, graphql_name='description')
    how_it_works = sgqlc.types.Field(String, graphql_name='howItWorks')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    primary_listing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='primaryListingCount')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    secondary_listing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='secondaryListingCount')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class MarketplaceListing(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('app', 'company_url', 'configuration_resource_path', 'configuration_url', 'documentation_url', 'extended_description', 'extended_description_html', 'full_description', 'full_description_html', 'has_published_free_trial_plans', 'has_terms_of_service', 'has_verified_owner', 'how_it_works', 'how_it_works_html', 'installation_url', 'installed_for_viewer', 'is_archived', 'is_draft', 'is_paid', 'is_public', 'is_rejected', 'is_unverified', 'is_unverified_pending', 'is_verification_pending_from_draft', 'is_verification_pending_from_unverified', 'is_verified', 'logo_background_color', 'logo_url', 'name', 'normalized_short_description', 'pricing_url', 'primary_category', 'privacy_policy_url', 'resource_path', 'screenshot_urls', 'secondary_category', 'short_description', 'slug', 'status_url', 'support_email', 'support_url', 'terms_of_service_url', 'url', 'viewer_can_add_plans', 'viewer_can_approve', 'viewer_can_delist', 'viewer_can_edit', 'viewer_can_edit_categories', 'viewer_can_edit_plans', 'viewer_can_redraft', 'viewer_can_reject', 'viewer_can_request_approval', 'viewer_has_purchased', 'viewer_has_purchased_for_all_organizations', 'viewer_is_listing_admin')
    app = sgqlc.types.Field(App, graphql_name='app')
    company_url = sgqlc.types.Field(URI, graphql_name='companyUrl')
    configuration_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='configurationResourcePath')
    configuration_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='configurationUrl')
    documentation_url = sgqlc.types.Field(URI, graphql_name='documentationUrl')
    extended_description = sgqlc.types.Field(String, graphql_name='extendedDescription')
    extended_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='extendedDescriptionHTML')
    full_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullDescription')
    full_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='fullDescriptionHTML')
    has_published_free_trial_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPublishedFreeTrialPlans')
    has_terms_of_service = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTermsOfService')
    has_verified_owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasVerifiedOwner')
    how_it_works = sgqlc.types.Field(String, graphql_name='howItWorks')
    how_it_works_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='howItWorksHTML')
    installation_url = sgqlc.types.Field(URI, graphql_name='installationUrl')
    installed_for_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='installedForViewer')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_paid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaid')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    is_rejected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRejected')
    is_unverified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnverified')
    is_unverified_pending = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnverifiedPending')
    is_verification_pending_from_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerificationPendingFromDraft')
    is_verification_pending_from_unverified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerificationPendingFromUnverified')
    is_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerified')
    logo_background_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoBackgroundColor')
    logo_url = sgqlc.types.Field(URI, graphql_name='logoUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=400)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    normalized_short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='normalizedShortDescription')
    pricing_url = sgqlc.types.Field(URI, graphql_name='pricingUrl')
    primary_category = sgqlc.types.Field(sgqlc.types.non_null(MarketplaceCategory), graphql_name='primaryCategory')
    privacy_policy_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='privacyPolicyUrl')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    screenshot_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='screenshotUrls')
    secondary_category = sgqlc.types.Field(MarketplaceCategory, graphql_name='secondaryCategory')
    short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortDescription')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    status_url = sgqlc.types.Field(URI, graphql_name='statusUrl')
    support_email = sgqlc.types.Field(String, graphql_name='supportEmail')
    support_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='supportUrl')
    terms_of_service_url = sgqlc.types.Field(URI, graphql_name='termsOfServiceUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_add_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAddPlans')
    viewer_can_approve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanApprove')
    viewer_can_delist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelist')
    viewer_can_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEdit')
    viewer_can_edit_categories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditCategories')
    viewer_can_edit_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditPlans')
    viewer_can_redraft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanRedraft')
    viewer_can_reject = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReject')
    viewer_can_request_approval = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanRequestApproval')
    viewer_has_purchased = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasPurchased')
    viewer_has_purchased_for_all_organizations = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasPurchasedForAllOrganizations')
    viewer_is_listing_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsListingAdmin')


class MemberFeatureRequestNotification(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('body', 'title', 'updated_at')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class MembersCanDeleteReposClearAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class MembersCanDeleteReposDisableAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class MembersCanDeleteReposEnableAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class MentionedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'database_id')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')


class MergeQueue(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('configuration', 'entries', 'next_entry_estimated_time_to_merge', 'repository', 'resource_path', 'url')
    configuration = sgqlc.types.Field(MergeQueueConfiguration, graphql_name='configuration')
    entries = sgqlc.types.Field(MergeQueueEntryConnection, graphql_name='entries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    next_entry_estimated_time_to_merge = sgqlc.types.Field(Int, graphql_name='nextEntryEstimatedTimeToMerge')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class MergeQueueEntry(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('base_commit', 'enqueued_at', 'enqueuer', 'estimated_time_to_merge', 'head_commit', 'jump', 'merge_queue', 'position', 'pull_request', 'solo', 'state')
    base_commit = sgqlc.types.Field(Commit, graphql_name='baseCommit')
    enqueued_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='enqueuedAt')
    enqueuer = sgqlc.types.Field(sgqlc.types.non_null(Actor), graphql_name='enqueuer')
    estimated_time_to_merge = sgqlc.types.Field(Int, graphql_name='estimatedTimeToMerge')
    head_commit = sgqlc.types.Field(Commit, graphql_name='headCommit')
    jump = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='jump')
    merge_queue = sgqlc.types.Field(MergeQueue, graphql_name='mergeQueue')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    solo = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='solo')
    state = sgqlc.types.Field(sgqlc.types.non_null(MergeQueueEntryState), graphql_name='state')


class MergedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('actor', 'commit', 'created_at', 'merge_ref', 'merge_ref_name', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    merge_ref = sgqlc.types.Field('Ref', graphql_name='mergeRef')
    merge_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mergeRefName')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class MigrationSource(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('name', 'type', 'url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(MigrationSourceType), graphql_name='type')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Milestone(sgqlc.types.Type, Closable, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('closed_issue_count', 'created_at', 'creator', 'description', 'description_html', 'due_on', 'issues', 'number', 'open_issue_count', 'progress_percentage', 'pull_requests', 'repository', 'state', 'title', 'updated_at')
    closed_issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='closedIssueCount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(String, graphql_name='descriptionHTML')
    due_on = sgqlc.types.Field(DateTime, graphql_name='dueOn')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    open_issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='openIssueCount')
    progress_percentage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='progressPercentage')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    state = sgqlc.types.Field(sgqlc.types.non_null(MilestoneState), graphql_name='state')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class MilestonedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'milestone_title', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    milestone_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='milestoneTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('MilestoneItem'), graphql_name='subject')


class MovedColumnsInProjectEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class OIDCProvider(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('enterprise', 'external_identities', 'provider_type', 'tenant_id')
    enterprise = sgqlc.types.Field(Enterprise, graphql_name='enterprise')
    external_identities = sgqlc.types.Field(sgqlc.types.non_null(ExternalIdentityConnection), graphql_name='externalIdentities', args=sgqlc.types.ArgDict((
        ('members_only', sgqlc.types.Arg(Boolean, graphql_name='membersOnly', default=None)),
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('user_name', sgqlc.types.Arg(String, graphql_name='userName', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    provider_type = sgqlc.types.Field(sgqlc.types.non_null(OIDCProviderType), graphql_name='providerType')
    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantId')


class OauthApplicationCreateAuditEntry(sgqlc.types.Type, AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgAddBillingManagerAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgAddMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgBlockUserAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgConfigDisableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgConfigEnableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgCreateAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgDisableOauthAppRestrictionsAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgDisableSamlAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgDisableTwoFactorRequirementAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgEnableOauthAppRestrictionsAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgEnableSamlAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgEnableTwoFactorRequirementAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgInviteMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgInviteToBusinessAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgOauthAppAccessApprovedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgOauthAppAccessBlockedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgOauthAppAccessDeniedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgOauthAppAccessRequestedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgOauthAppAccessUnblockedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRemoveBillingManagerAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRemoveMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRemoveOutsideCollaboratorAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRestoreMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRestoreMemberMembershipOrganizationAuditEntryData(sgqlc.types.Type, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRestoreMemberMembershipRepositoryAuditEntryData(sgqlc.types.Type, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgRestoreMemberMembershipTeamAuditEntryData(sgqlc.types.Type, TeamAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgUnblockUserAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgUpdateDefaultRepositoryPermissionAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgUpdateMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgUpdateMemberRepositoryCreationPermissionAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class OrgUpdateMemberRepositoryInvitationPermissionAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class Organization(sgqlc.types.Type, Actor, MemberStatusable, Node, PackageOwner, ProfileOwner, ProjectOwner, ProjectV2Owner, ProjectV2Recent, RepositoryDiscussionAuthor, RepositoryDiscussionCommentAuthor, RepositoryOwner, Sponsorable, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('announcement_banner', 'archived_at', 'created_at', 'database_id', 'description', 'description_html', 'domains', 'enterprise_owners', 'interaction_ability', 'ip_allow_list_enabled_setting', 'ip_allow_list_entries', 'ip_allow_list_for_installed_apps_enabled_setting', 'is_verified', 'issue_types', 'mannequins', 'members_can_fork_private_repositories', 'members_with_role', 'new_team_resource_path', 'new_team_url', 'notification_delivery_restriction_enabled_setting', 'organization_billing_email', 'pending_members', 'projects_resource_path', 'projects_url', 'repository_migrations', 'requires_two_factor_authentication', 'ruleset', 'rulesets', 'saml_identity_provider', 'team', 'teams', 'teams_resource_path', 'teams_url', 'twitter_username', 'updated_at', 'viewer_can_administer', 'viewer_can_create_repositories', 'viewer_can_create_teams', 'viewer_is_amember', 'viewer_is_following', 'web_commit_signoff_required')
    announcement_banner = sgqlc.types.Field(AnnouncementBanner, graphql_name='announcementBanner')
    archived_at = sgqlc.types.Field(DateTime, graphql_name='archivedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(String, graphql_name='descriptionHTML')
    domains = sgqlc.types.Field(VerifiableDomainConnection, graphql_name='domains', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_verified', sgqlc.types.Arg(Boolean, graphql_name='isVerified', default=None)),
        ('is_approved', sgqlc.types.Arg(Boolean, graphql_name='isApproved', default=None)),
        ('order_by', sgqlc.types.Arg(VerifiableDomainOrder, graphql_name='orderBy', default={'field': 'DOMAIN', 'direction': 'ASC'})),
))
    )
    enterprise_owners = sgqlc.types.Field(sgqlc.types.non_null(OrganizationEnterpriseOwnerConnection), graphql_name='enterpriseOwners', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('organization_role', sgqlc.types.Arg(RoleInOrganization, graphql_name='organizationRole', default=None)),
        ('order_by', sgqlc.types.Arg(OrgEnterpriseOwnerOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    interaction_ability = sgqlc.types.Field(RepositoryInteractionAbility, graphql_name='interactionAbility')
    ip_allow_list_enabled_setting = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListEnabledSettingValue), graphql_name='ipAllowListEnabledSetting')
    ip_allow_list_entries = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListEntryConnection), graphql_name='ipAllowListEntries', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(IpAllowListEntryOrder, graphql_name='orderBy', default={'field': 'ALLOW_LIST_VALUE', 'direction': 'ASC'})),
))
    )
    ip_allow_list_for_installed_apps_enabled_setting = sgqlc.types.Field(sgqlc.types.non_null(IpAllowListForInstalledAppsEnabledSettingValue), graphql_name='ipAllowListForInstalledAppsEnabledSetting')
    is_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerified')
    issue_types = sgqlc.types.Field(IssueTypeConnection, graphql_name='issueTypes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(IssueTypeOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )
    mannequins = sgqlc.types.Field(sgqlc.types.non_null(MannequinConnection), graphql_name='mannequins', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('order_by', sgqlc.types.Arg(MannequinOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )
    members_can_fork_private_repositories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='membersCanForkPrivateRepositories')
    members_with_role = sgqlc.types.Field(sgqlc.types.non_null(OrganizationMemberConnection), graphql_name='membersWithRole', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    new_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamResourcePath')
    new_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamUrl')
    notification_delivery_restriction_enabled_setting = sgqlc.types.Field(sgqlc.types.non_null(NotificationRestrictionSettingValue), graphql_name='notificationDeliveryRestrictionEnabledSetting')
    organization_billing_email = sgqlc.types.Field(String, graphql_name='organizationBillingEmail')
    pending_members = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='pendingMembers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    repository_migrations = sgqlc.types.Field(sgqlc.types.non_null(RepositoryMigrationConnection), graphql_name='repositoryMigrations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(MigrationState, graphql_name='state', default=None)),
        ('repository_name', sgqlc.types.Arg(String, graphql_name='repositoryName', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryMigrationOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )
    requires_two_factor_authentication = sgqlc.types.Field(Boolean, graphql_name='requiresTwoFactorAuthentication')
    ruleset = sgqlc.types.Field('RepositoryRuleset', graphql_name='ruleset', args=sgqlc.types.ArgDict((
        ('database_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='databaseId', default=None)),
        ('include_parents', sgqlc.types.Arg(Boolean, graphql_name='includeParents', default=True)),
))
    )
    rulesets = sgqlc.types.Field(RepositoryRulesetConnection, graphql_name='rulesets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_parents', sgqlc.types.Arg(Boolean, graphql_name='includeParents', default=True)),
        ('targets', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryRulesetTarget)), graphql_name='targets', default=None)),
))
    )
    saml_identity_provider = sgqlc.types.Field('OrganizationIdentityProvider', graphql_name='samlIdentityProvider')
    team = sgqlc.types.Field('Team', graphql_name='team', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(TeamPrivacy, graphql_name='privacy', default=None)),
        ('notification_setting', sgqlc.types.Arg(TeamNotificationSetting, graphql_name='notificationSetting', default=None)),
        ('role', sgqlc.types.Arg(TeamRole, graphql_name='role', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('user_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userLogins', default=None)),
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default=None)),
        ('ldap_mapped', sgqlc.types.Arg(Boolean, graphql_name='ldapMapped', default=None)),
        ('root_teams_only', sgqlc.types.Arg(Boolean, graphql_name='rootTeamsOnly', default=False)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    twitter_username = sgqlc.types.Field(String, graphql_name='twitterUsername')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_create_repositories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateRepositories')
    viewer_can_create_teams = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateTeams')
    viewer_is_amember = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsAMember')
    viewer_is_following = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsFollowing')
    web_commit_signoff_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webCommitSignoffRequired')


class OrganizationIdentityProvider(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('digest_method', 'external_identities', 'idp_certificate', 'issuer', 'organization', 'signature_method', 'sso_url')
    digest_method = sgqlc.types.Field(URI, graphql_name='digestMethod')
    external_identities = sgqlc.types.Field(sgqlc.types.non_null(ExternalIdentityConnection), graphql_name='externalIdentities', args=sgqlc.types.ArgDict((
        ('members_only', sgqlc.types.Arg(Boolean, graphql_name='membersOnly', default=None)),
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('user_name', sgqlc.types.Arg(String, graphql_name='userName', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    idp_certificate = sgqlc.types.Field(X509Certificate, graphql_name='idpCertificate')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    signature_method = sgqlc.types.Field(URI, graphql_name='signatureMethod')
    sso_url = sgqlc.types.Field(URI, graphql_name='ssoUrl')


class OrganizationInvitation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'email', 'invitation_source', 'invitation_type', 'invitee', 'inviter_actor', 'organization', 'role')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    invitation_source = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationSource), graphql_name='invitationSource')
    invitation_type = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationType), graphql_name='invitationType')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    inviter_actor = sgqlc.types.Field('User', graphql_name='inviterActor')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    role = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationRole), graphql_name='role')


class OrganizationMigration(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'database_id', 'failure_reason', 'remaining_repositories_count', 'source_org_name', 'source_org_url', 'state', 'target_org_name', 'total_repositories_count')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(String, graphql_name='databaseId')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    remaining_repositories_count = sgqlc.types.Field(Int, graphql_name='remainingRepositoriesCount')
    source_org_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceOrgName')
    source_org_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='sourceOrgUrl')
    state = sgqlc.types.Field(sgqlc.types.non_null(OrganizationMigrationState), graphql_name='state')
    target_org_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetOrgName')
    total_repositories_count = sgqlc.types.Field(Int, graphql_name='totalRepositoriesCount')


class OrganizationTeamsHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = schema
    __field_names__ = ('relevant_teams', 'teams_resource_path', 'teams_url', 'total_team_count')
    relevant_teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='relevantTeams', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    total_team_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalTeamCount')


class OrganizationsHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = schema
    __field_names__ = ('relevant_organizations', 'total_organization_count')
    relevant_organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='relevantOrganizations', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    total_organization_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalOrganizationCount')


class Package(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('latest_version', 'name', 'package_type', 'repository', 'statistics', 'version', 'versions')
    latest_version = sgqlc.types.Field('PackageVersion', graphql_name='latestVersion')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    package_type = sgqlc.types.Field(sgqlc.types.non_null(PackageType), graphql_name='packageType')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    statistics = sgqlc.types.Field(PackageStatistics, graphql_name='statistics')
    version = sgqlc.types.Field('PackageVersion', graphql_name='version', args=sgqlc.types.ArgDict((
        ('version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='version', default=None)),
))
    )
    versions = sgqlc.types.Field(sgqlc.types.non_null(PackageVersionConnection), graphql_name='versions', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(PackageVersionOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class PackageFile(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('md5', 'name', 'package_version', 'sha1', 'sha256', 'size', 'updated_at', 'url')
    md5 = sgqlc.types.Field(String, graphql_name='md5')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    package_version = sgqlc.types.Field('PackageVersion', graphql_name='packageVersion')
    sha1 = sgqlc.types.Field(String, graphql_name='sha1')
    sha256 = sgqlc.types.Field(String, graphql_name='sha256')
    size = sgqlc.types.Field(Int, graphql_name='size')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(URI, graphql_name='url')


class PackageTag(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('name', 'version')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    version = sgqlc.types.Field('PackageVersion', graphql_name='version')


class PackageVersion(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('files', 'package', 'platform', 'pre_release', 'readme', 'release', 'statistics', 'summary', 'version')
    files = sgqlc.types.Field(sgqlc.types.non_null(PackageFileConnection), graphql_name='files', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(PackageFileOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    package = sgqlc.types.Field(Package, graphql_name='package')
    platform = sgqlc.types.Field(String, graphql_name='platform')
    pre_release = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='preRelease')
    readme = sgqlc.types.Field(String, graphql_name='readme')
    release = sgqlc.types.Field('Release', graphql_name='release')
    statistics = sgqlc.types.Field(PackageVersionStatistics, graphql_name='statistics')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='version')


class ParentIssueAddedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'parent')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    parent = sgqlc.types.Field(Issue, graphql_name='parent')


class ParentIssueRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'parent')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    parent = sgqlc.types.Field(Issue, graphql_name='parent')


class PinnedDiscussion(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = schema
    __field_names__ = ('created_at', 'database_id', 'discussion', 'gradient_stop_colors', 'pattern', 'pinned_by', 'preconfigured_gradient', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    discussion = sgqlc.types.Field(sgqlc.types.non_null(Discussion), graphql_name='discussion')
    gradient_stop_colors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='gradientStopColors')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(PinnedDiscussionPattern), graphql_name='pattern')
    pinned_by = sgqlc.types.Field(sgqlc.types.non_null(Actor), graphql_name='pinnedBy')
    preconfigured_gradient = sgqlc.types.Field(PinnedDiscussionGradient, graphql_name='preconfiguredGradient')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PinnedEnvironment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'database_id', 'environment', 'position', 'repository')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    environment = sgqlc.types.Field(sgqlc.types.non_null(Environment), graphql_name='environment')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PinnedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'issue')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')


class PinnedIssue(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('database_id', 'full_database_id', 'issue', 'pinned_by', 'repository')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    pinned_by = sgqlc.types.Field(sgqlc.types.non_null(Actor), graphql_name='pinnedBy')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PrivateRepositoryForkingDisableAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class PrivateRepositoryForkingEnableAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class Project(sgqlc.types.Type, Closable, Node, Updatable):
    __schema__ = schema
    __field_names__ = ()


class ProjectCard(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ()


class ProjectColumn(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ()


class ProjectV2(sgqlc.types.Type, Closable, Node, Updatable):
    __schema__ = schema
    __field_names__ = ('created_at', 'creator', 'field', 'fields', 'full_database_id', 'items', 'number', 'owner', 'public', 'readme', 'repositories', 'resource_path', 'short_description', 'status_updates', 'teams', 'template', 'title', 'updated_at', 'url', 'view', 'views', 'workflow', 'workflows')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    field = sgqlc.types.Field('ProjectV2FieldConfiguration', graphql_name='field', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    fields = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2FieldConfigurationConnection), graphql_name='fields', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2FieldOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    items = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2ItemOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default='')),
))
    )
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    owner = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2Owner), graphql_name='owner')
    public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='public')
    readme = sgqlc.types.Field(String, graphql_name='readme')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')
    status_updates = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2StatusUpdateConnection), graphql_name='statusUpdates', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2StatusOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
))
    )
    template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='template')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    view = sgqlc.types.Field('ProjectV2View', graphql_name='view', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    views = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ViewConnection), graphql_name='views', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2ViewOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )
    workflow = sgqlc.types.Field('ProjectV2Workflow', graphql_name='workflow', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    workflows = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2WorkflowConnection), graphql_name='workflows', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2WorkflowOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
))
    )


class ProjectV2Field(sgqlc.types.Type, Node, ProjectV2FieldCommon):
    __schema__ = schema
    __field_names__ = ()


class ProjectV2Item(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('content', 'created_at', 'creator', 'field_value_by_name', 'field_values', 'full_database_id', 'is_archived', 'project', 'type', 'updated_at')
    content = sgqlc.types.Field('ProjectV2ItemContent', graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    field_value_by_name = sgqlc.types.Field('ProjectV2ItemFieldValue', graphql_name='fieldValueByName', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    field_values = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemFieldValueConnection), graphql_name='fieldValues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2ItemFieldValueOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2), graphql_name='project')
    type = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemType), graphql_name='type')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class ProjectV2ItemFieldDateValue(sgqlc.types.Type, Node, ProjectV2ItemFieldValueCommon):
    __schema__ = schema
    __field_names__ = ('date',)
    date = sgqlc.types.Field(Date, graphql_name='date')


class ProjectV2ItemFieldIterationValue(sgqlc.types.Type, Node, ProjectV2ItemFieldValueCommon):
    __schema__ = schema
    __field_names__ = ('duration', 'iteration_id', 'start_date', 'title', 'title_html')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    iteration_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iterationId')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='startDate')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    title_html = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='titleHTML')


class ProjectV2ItemFieldNumberValue(sgqlc.types.Type, Node, ProjectV2ItemFieldValueCommon):
    __schema__ = schema
    __field_names__ = ('number',)
    number = sgqlc.types.Field(Float, graphql_name='number')


class ProjectV2ItemFieldSingleSelectValue(sgqlc.types.Type, Node, ProjectV2ItemFieldValueCommon):
    __schema__ = schema
    __field_names__ = ('color', 'description', 'description_html', 'name', 'name_html', 'option_id')
    color = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2SingleSelectFieldOptionColor), graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(String, graphql_name='descriptionHTML')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_html = sgqlc.types.Field(String, graphql_name='nameHTML')
    option_id = sgqlc.types.Field(String, graphql_name='optionId')


class ProjectV2ItemFieldTextValue(sgqlc.types.Type, Node, ProjectV2ItemFieldValueCommon):
    __schema__ = schema
    __field_names__ = ('text',)
    text = sgqlc.types.Field(String, graphql_name='text')


class ProjectV2ItemStatusChangedEvent(sgqlc.types.Type, Node, ProjectV2Event):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'previous_status', 'status')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    previous_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='previousStatus')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')


class ProjectV2IterationField(sgqlc.types.Type, Node, ProjectV2FieldCommon):
    __schema__ = schema
    __field_names__ = ('configuration',)
    configuration = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2IterationFieldConfiguration), graphql_name='configuration')


class ProjectV2SingleSelectField(sgqlc.types.Type, Node, ProjectV2FieldCommon):
    __schema__ = schema
    __field_names__ = ('options',)
    options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectV2SingleSelectFieldOption))), graphql_name='options', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='names', default=None)),
))
    )


class ProjectV2StatusUpdate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('body', 'body_html', 'created_at', 'creator', 'full_database_id', 'project', 'start_date', 'status', 'target_date', 'updated_at')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_html = sgqlc.types.Field(HTML, graphql_name='bodyHTML')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2), graphql_name='project')
    start_date = sgqlc.types.Field(Date, graphql_name='startDate')
    status = sgqlc.types.Field(ProjectV2StatusUpdateStatus, graphql_name='status')
    target_date = sgqlc.types.Field(Date, graphql_name='targetDate')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class ProjectV2View(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'fields', 'filter', 'full_database_id', 'group_by_fields', 'layout', 'name', 'number', 'project', 'sort_by_fields', 'updated_at', 'vertical_group_by_fields')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    fields = sgqlc.types.Field(ProjectV2FieldConfigurationConnection, graphql_name='fields', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2FieldOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )
    filter = sgqlc.types.Field(String, graphql_name='filter')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    group_by_fields = sgqlc.types.Field(ProjectV2FieldConfigurationConnection, graphql_name='groupByFields', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2FieldOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )
    layout = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ViewLayout), graphql_name='layout')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2), graphql_name='project')
    sort_by_fields = sgqlc.types.Field(ProjectV2SortByFieldConnection, graphql_name='sortByFields', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    vertical_group_by_fields = sgqlc.types.Field(ProjectV2FieldConfigurationConnection, graphql_name='verticalGroupByFields', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2FieldOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )


class ProjectV2Workflow(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'enabled', 'full_database_id', 'name', 'number', 'project', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2), graphql_name='project')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PublicKey(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('accessed_at', 'created_at', 'fingerprint', 'is_read_only', 'key', 'updated_at')
    accessed_at = sgqlc.types.Field(DateTime, graphql_name='accessedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    fingerprint = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fingerprint')
    is_read_only = sgqlc.types.Field(Boolean, graphql_name='isReadOnly')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')


class PullRequest(sgqlc.types.Type, Assignable, Closable, Comment, Labelable, Lockable, Node, ProjectV2Owner, Reactable, RepositoryNode, Subscribable, UniformResourceLocatable, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('additions', 'auto_merge_request', 'base_ref', 'base_ref_name', 'base_ref_oid', 'base_repository', 'can_be_rebased', 'changed_files', 'checks_resource_path', 'checks_url', 'closing_issues_references', 'comments', 'commits', 'deletions', 'files', 'full_database_id', 'head_ref', 'head_ref_name', 'head_ref_oid', 'head_repository', 'head_repository_owner', 'hovercard', 'is_cross_repository', 'is_draft', 'is_in_merge_queue', 'is_merge_queue_enabled', 'is_read_by_viewer', 'latest_opinionated_reviews', 'latest_reviews', 'maintainer_can_modify', 'merge_commit', 'merge_queue', 'merge_queue_entry', 'merge_state_status', 'mergeable', 'merged', 'merged_at', 'merged_by', 'milestone', 'number', 'participants', 'permalink', 'potential_merge_commit', 'project_items', 'revert_resource_path', 'revert_url', 'review_decision', 'review_requests', 'review_threads', 'reviews', 'state', 'status_check_rollup', 'suggested_reviewers', 'timeline_items', 'title', 'title_html', 'total_comments_count', 'viewer_can_apply_suggestion', 'viewer_can_delete_head_ref', 'viewer_can_disable_auto_merge', 'viewer_can_edit_files', 'viewer_can_enable_auto_merge', 'viewer_can_merge_as_admin', 'viewer_can_update_branch', 'viewer_latest_review', 'viewer_latest_review_request', 'viewer_merge_body_text', 'viewer_merge_headline_text')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    auto_merge_request = sgqlc.types.Field(AutoMergeRequest, graphql_name='autoMergeRequest')
    base_ref = sgqlc.types.Field('Ref', graphql_name='baseRef')
    base_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='baseRefName')
    base_ref_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='baseRefOid')
    base_repository = sgqlc.types.Field('Repository', graphql_name='baseRepository')
    can_be_rebased = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canBeRebased')
    changed_files = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='changedFiles')
    checks_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='checksResourcePath')
    checks_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='checksUrl')
    closing_issues_references = sgqlc.types.Field(IssueConnection, graphql_name='closingIssuesReferences', args=sgqlc.types.ArgDict((
        ('user_linked_only', sgqlc.types.Arg(Boolean, graphql_name='userLinkedOnly', default=False)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueCommentOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commits = sgqlc.types.Field(sgqlc.types.non_null(PullRequestCommitConnection), graphql_name='commits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    files = sgqlc.types.Field(PullRequestChangedFileConnection, graphql_name='files', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    head_ref = sgqlc.types.Field('Ref', graphql_name='headRef')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    head_ref_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='headRefOid')
    head_repository = sgqlc.types.Field('Repository', graphql_name='headRepository')
    head_repository_owner = sgqlc.types.Field(RepositoryOwner, graphql_name='headRepositoryOwner')
    hovercard = sgqlc.types.Field(sgqlc.types.non_null(Hovercard), graphql_name='hovercard', args=sgqlc.types.ArgDict((
        ('include_notification_contexts', sgqlc.types.Arg(Boolean, graphql_name='includeNotificationContexts', default=True)),
))
    )
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_in_merge_queue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInMergeQueue')
    is_merge_queue_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMergeQueueEnabled')
    is_read_by_viewer = sgqlc.types.Field(Boolean, graphql_name='isReadByViewer')
    latest_opinionated_reviews = sgqlc.types.Field(PullRequestReviewConnection, graphql_name='latestOpinionatedReviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('writers_only', sgqlc.types.Arg(Boolean, graphql_name='writersOnly', default=False)),
))
    )
    latest_reviews = sgqlc.types.Field(PullRequestReviewConnection, graphql_name='latestReviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    maintainer_can_modify = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='maintainerCanModify')
    merge_commit = sgqlc.types.Field(Commit, graphql_name='mergeCommit')
    merge_queue = sgqlc.types.Field(MergeQueue, graphql_name='mergeQueue')
    merge_queue_entry = sgqlc.types.Field(MergeQueueEntry, graphql_name='mergeQueueEntry')
    merge_state_status = sgqlc.types.Field(sgqlc.types.non_null(MergeStateStatus), graphql_name='mergeStateStatus')
    mergeable = sgqlc.types.Field(sgqlc.types.non_null(MergeableState), graphql_name='mergeable')
    merged = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='merged')
    merged_at = sgqlc.types.Field(DateTime, graphql_name='mergedAt')
    merged_by = sgqlc.types.Field(Actor, graphql_name='mergedBy')
    milestone = sgqlc.types.Field(Milestone, graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    participants = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    permalink = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='permalink')
    potential_merge_commit = sgqlc.types.Field(Commit, graphql_name='potentialMergeCommit')
    project_items = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2ItemConnection), graphql_name='projectItems', args=sgqlc.types.ArgDict((
        ('include_archived', sgqlc.types.Arg(Boolean, graphql_name='includeArchived', default=True)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    revert_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='revertResourcePath')
    revert_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='revertUrl')
    review_decision = sgqlc.types.Field(PullRequestReviewDecision, graphql_name='reviewDecision')
    review_requests = sgqlc.types.Field(ReviewRequestConnection, graphql_name='reviewRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    review_threads = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewThreadConnection), graphql_name='reviewThreads', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    reviews = sgqlc.types.Field(PullRequestReviewConnection, graphql_name='reviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestReviewState)), graphql_name='states', default=None)),
        ('author', sgqlc.types.Arg(String, graphql_name='author', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestState), graphql_name='state')
    status_check_rollup = sgqlc.types.Field('StatusCheckRollup', graphql_name='statusCheckRollup')
    suggested_reviewers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SuggestedReviewer)), graphql_name='suggestedReviewers')
    timeline_items = sgqlc.types.Field(sgqlc.types.non_null(PullRequestTimelineItemsConnection), graphql_name='timelineItems', args=sgqlc.types.ArgDict((
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('item_types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestTimelineItemsItemType)), graphql_name='itemTypes', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    title_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='titleHTML')
    total_comments_count = sgqlc.types.Field(Int, graphql_name='totalCommentsCount')
    viewer_can_apply_suggestion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanApplySuggestion')
    viewer_can_delete_head_ref = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDeleteHeadRef')
    viewer_can_disable_auto_merge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDisableAutoMerge')
    viewer_can_edit_files = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditFiles')
    viewer_can_enable_auto_merge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEnableAutoMerge')
    viewer_can_merge_as_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMergeAsAdmin')
    viewer_can_update_branch = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdateBranch')
    viewer_latest_review = sgqlc.types.Field('PullRequestReview', graphql_name='viewerLatestReview')
    viewer_latest_review_request = sgqlc.types.Field('ReviewRequest', graphql_name='viewerLatestReviewRequest')
    viewer_merge_body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='viewerMergeBodyText', args=sgqlc.types.ArgDict((
        ('merge_type', sgqlc.types.Arg(PullRequestMergeMethod, graphql_name='mergeType', default=None)),
))
    )
    viewer_merge_headline_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='viewerMergeHeadlineText', args=sgqlc.types.ArgDict((
        ('merge_type', sgqlc.types.Arg(PullRequestMergeMethod, graphql_name='mergeType', default=None)),
))
    )


class PullRequestCommit(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('commit', 'pull_request')
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')


class PullRequestCommitCommentThread(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = schema
    __field_names__ = ('comments', 'commit', 'path', 'position', 'pull_request')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')


class PullRequestReview(sgqlc.types.Type, Comment, Deletable, Minimizable, Node, Reactable, RepositoryNode, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('author_can_push_to_repository', 'comments', 'commit', 'full_database_id', 'on_behalf_of', 'pull_request', 'resource_path', 'state', 'submitted_at', 'url')
    author_can_push_to_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='authorCanPushToRepository')
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    on_behalf_of = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='onBehalfOf', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='state')
    submitted_at = sgqlc.types.Field(DateTime, graphql_name='submittedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class PullRequestReviewComment(sgqlc.types.Type, Comment, Deletable, Minimizable, Node, Reactable, RepositoryNode, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ('commit', 'diff_hunk', 'drafted_at', 'full_database_id', 'line', 'original_commit', 'original_line', 'original_start_line', 'outdated', 'path', 'pull_request', 'pull_request_review', 'reply_to', 'resource_path', 'start_line', 'state', 'subject_type', 'url')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    diff_hunk = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='diffHunk')
    drafted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='draftedAt')
    full_database_id = sgqlc.types.Field(BigInt, graphql_name='fullDatabaseId')
    line = sgqlc.types.Field(Int, graphql_name='line')
    original_commit = sgqlc.types.Field(Commit, graphql_name='originalCommit')
    original_line = sgqlc.types.Field(Int, graphql_name='originalLine')
    original_start_line = sgqlc.types.Field(Int, graphql_name='originalStartLine')
    outdated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='outdated')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    pull_request_review = sgqlc.types.Field(PullRequestReview, graphql_name='pullRequestReview')
    reply_to = sgqlc.types.Field('PullRequestReviewComment', graphql_name='replyTo')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    start_line = sgqlc.types.Field(Int, graphql_name='startLine')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentState), graphql_name='state')
    subject_type = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewThreadSubjectType), graphql_name='subjectType')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class PullRequestReviewThread(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('comments', 'diff_side', 'is_collapsed', 'is_outdated', 'is_resolved', 'line', 'original_line', 'original_start_line', 'path', 'pull_request', 'repository', 'resolved_by', 'start_diff_side', 'start_line', 'subject_type', 'viewer_can_reply', 'viewer_can_resolve', 'viewer_can_unresolve')
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    diff_side = sgqlc.types.Field(sgqlc.types.non_null(DiffSide), graphql_name='diffSide')
    is_collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCollapsed')
    is_outdated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOutdated')
    is_resolved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isResolved')
    line = sgqlc.types.Field(Int, graphql_name='line')
    original_line = sgqlc.types.Field(Int, graphql_name='originalLine')
    original_start_line = sgqlc.types.Field(Int, graphql_name='originalStartLine')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resolved_by = sgqlc.types.Field('User', graphql_name='resolvedBy')
    start_diff_side = sgqlc.types.Field(DiffSide, graphql_name='startDiffSide')
    start_line = sgqlc.types.Field(Int, graphql_name='startLine')
    subject_type = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewThreadSubjectType), graphql_name='subjectType')
    viewer_can_reply = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReply')
    viewer_can_resolve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanResolve')
    viewer_can_unresolve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUnresolve')


class PullRequestThread(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('comments', 'diff_side', 'is_collapsed', 'is_outdated', 'is_resolved', 'line', 'path', 'pull_request', 'repository', 'resolved_by', 'start_diff_side', 'start_line', 'subject_type', 'viewer_can_reply', 'viewer_can_resolve', 'viewer_can_unresolve')
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    diff_side = sgqlc.types.Field(sgqlc.types.non_null(DiffSide), graphql_name='diffSide')
    is_collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCollapsed')
    is_outdated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOutdated')
    is_resolved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isResolved')
    line = sgqlc.types.Field(Int, graphql_name='line')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resolved_by = sgqlc.types.Field('User', graphql_name='resolvedBy')
    start_diff_side = sgqlc.types.Field(DiffSide, graphql_name='startDiffSide')
    start_line = sgqlc.types.Field(Int, graphql_name='startLine')
    subject_type = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewThreadSubjectType), graphql_name='subjectType')
    viewer_can_reply = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReply')
    viewer_can_resolve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanResolve')
    viewer_can_unresolve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUnresolve')


class Push(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('next_sha', 'permalink', 'previous_sha', 'pusher', 'repository')
    next_sha = sgqlc.types.Field(GitObjectID, graphql_name='nextSha')
    permalink = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='permalink')
    previous_sha = sgqlc.types.Field(GitObjectID, graphql_name='previousSha')
    pusher = sgqlc.types.Field(sgqlc.types.non_null(Actor), graphql_name='pusher')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PushAllowance(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'branch_protection_rule')
    actor = sgqlc.types.Field('PushAllowanceActor', graphql_name='actor')
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')


class Query(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('code_of_conduct', 'codes_of_conduct', 'enterprise', 'enterprise_administrator_invitation', 'enterprise_administrator_invitation_by_token', 'enterprise_member_invitation', 'enterprise_member_invitation_by_token', 'license', 'licenses', 'marketplace_categories', 'marketplace_category', 'marketplace_listing', 'marketplace_listings', 'meta', 'node', 'nodes', 'organization', 'rate_limit', 'relay', 'repository', 'repository_owner', 'resource', 'search', 'security_advisories', 'security_advisory', 'security_vulnerabilities', 'sponsorables', 'topic', 'user', 'viewer')
    code_of_conduct = sgqlc.types.Field(CodeOfConduct, graphql_name='codeOfConduct', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    codes_of_conduct = sgqlc.types.Field(sgqlc.types.list_of(CodeOfConduct), graphql_name='codesOfConduct')
    enterprise = sgqlc.types.Field(Enterprise, graphql_name='enterprise', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('invitation_token', sgqlc.types.Arg(String, graphql_name='invitationToken', default=None)),
))
    )
    enterprise_administrator_invitation = sgqlc.types.Field(EnterpriseAdministratorInvitation, graphql_name='enterpriseAdministratorInvitation', args=sgqlc.types.ArgDict((
        ('user_login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userLogin', default=None)),
        ('enterprise_slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='enterpriseSlug', default=None)),
        ('role', sgqlc.types.Arg(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role', default=None)),
))
    )
    enterprise_administrator_invitation_by_token = sgqlc.types.Field(EnterpriseAdministratorInvitation, graphql_name='enterpriseAdministratorInvitationByToken', args=sgqlc.types.ArgDict((
        ('invitation_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invitationToken', default=None)),
))
    )
    enterprise_member_invitation = sgqlc.types.Field(EnterpriseMemberInvitation, graphql_name='enterpriseMemberInvitation', args=sgqlc.types.ArgDict((
        ('user_login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userLogin', default=None)),
        ('enterprise_slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='enterpriseSlug', default=None)),
))
    )
    enterprise_member_invitation_by_token = sgqlc.types.Field(EnterpriseMemberInvitation, graphql_name='enterpriseMemberInvitationByToken', args=sgqlc.types.ArgDict((
        ('invitation_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invitationToken', default=None)),
))
    )
    license = sgqlc.types.Field(License, graphql_name='license', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    licenses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(License)), graphql_name='licenses')
    marketplace_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MarketplaceCategory))), graphql_name='marketplaceCategories', args=sgqlc.types.ArgDict((
        ('include_categories', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='includeCategories', default=None)),
        ('exclude_empty', sgqlc.types.Arg(Boolean, graphql_name='excludeEmpty', default=None)),
        ('exclude_subcategories', sgqlc.types.Arg(Boolean, graphql_name='excludeSubcategories', default=None)),
))
    )
    marketplace_category = sgqlc.types.Field(MarketplaceCategory, graphql_name='marketplaceCategory', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('use_topic_aliases', sgqlc.types.Arg(Boolean, graphql_name='useTopicAliases', default=None)),
))
    )
    marketplace_listing = sgqlc.types.Field(MarketplaceListing, graphql_name='marketplaceListing', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    marketplace_listings = sgqlc.types.Field(sgqlc.types.non_null(MarketplaceListingConnection), graphql_name='marketplaceListings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('category_slug', sgqlc.types.Arg(String, graphql_name='categorySlug', default=None)),
        ('use_topic_aliases', sgqlc.types.Arg(Boolean, graphql_name='useTopicAliases', default=None)),
        ('viewer_can_admin', sgqlc.types.Arg(Boolean, graphql_name='viewerCanAdmin', default=None)),
        ('admin_id', sgqlc.types.Arg(ID, graphql_name='adminId', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationId', default=None)),
        ('all_states', sgqlc.types.Arg(Boolean, graphql_name='allStates', default=None)),
        ('slugs', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='slugs', default=None)),
        ('primary_category_only', sgqlc.types.Arg(Boolean, graphql_name='primaryCategoryOnly', default=False)),
        ('with_free_trials_only', sgqlc.types.Arg(Boolean, graphql_name='withFreeTrialsOnly', default=False)),
))
    )
    meta = sgqlc.types.Field(sgqlc.types.non_null(GitHubMetadata), graphql_name='meta')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Node)), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    organization = sgqlc.types.Field(Organization, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    rate_limit = sgqlc.types.Field(RateLimit, graphql_name='rateLimit', args=sgqlc.types.ArgDict((
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=False)),
))
    )
    relay = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='relay')
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('owner', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='owner', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('follow_renames', sgqlc.types.Arg(Boolean, graphql_name='followRenames', default=True)),
))
    )
    repository_owner = sgqlc.types.Field(RepositoryOwner, graphql_name='repositoryOwner', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    resource = sgqlc.types.Field(UniformResourceLocatable, graphql_name='resource', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(URI), graphql_name='url', default=None)),
))
    )
    search = sgqlc.types.Field(sgqlc.types.non_null(SearchResultItemConnection), graphql_name='search', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(SearchType), graphql_name='type', default=None)),
))
    )
    security_advisories = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryConnection), graphql_name='securityAdvisories', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(SecurityAdvisoryOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('identifier', sgqlc.types.Arg(SecurityAdvisoryIdentifierFilter, graphql_name='identifier', default=None)),
        ('published_since', sgqlc.types.Arg(DateTime, graphql_name='publishedSince', default=None)),
        ('updated_since', sgqlc.types.Arg(DateTime, graphql_name='updatedSince', default=None)),
        ('classifications', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryClassification)), graphql_name='classifications', default=None)),
        ('epss_percentage', sgqlc.types.Arg(Float, graphql_name='epssPercentage', default=None)),
        ('epss_percentile', sgqlc.types.Arg(Float, graphql_name='epssPercentile', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    security_advisory = sgqlc.types.Field('SecurityAdvisory', graphql_name='securityAdvisory', args=sgqlc.types.ArgDict((
        ('ghsa_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='ghsaId', default=None)),
))
    )
    security_vulnerabilities = sgqlc.types.Field(sgqlc.types.non_null(SecurityVulnerabilityConnection), graphql_name='securityVulnerabilities', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(SecurityVulnerabilityOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('ecosystem', sgqlc.types.Arg(SecurityAdvisoryEcosystem, graphql_name='ecosystem', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('severities', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisorySeverity)), graphql_name='severities', default=None)),
        ('classifications', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryClassification)), graphql_name='classifications', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sponsorables = sgqlc.types.Field(sgqlc.types.non_null(SponsorableItemConnection), graphql_name='sponsorables', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorableOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('only_dependencies', sgqlc.types.Arg(Boolean, graphql_name='onlyDependencies', default=False)),
        ('org_login_for_dependencies', sgqlc.types.Arg(String, graphql_name='orgLoginForDependencies', default=None)),
        ('dependency_ecosystem', sgqlc.types.Arg(SecurityAdvisoryEcosystem, graphql_name='dependencyEcosystem', default=None)),
        ('ecosystem', sgqlc.types.Arg(DependencyGraphEcosystem, graphql_name='ecosystem', default=None)),
))
    )
    topic = sgqlc.types.Field('Topic', graphql_name='topic', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    viewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='viewer')


class Reaction(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('content', 'created_at', 'database_id', 'reactable', 'user')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    reactable = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='reactable')
    user = sgqlc.types.Field('User', graphql_name='user')


class ReadyForReviewEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'pull_request')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')


class Ref(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('associated_pull_requests', 'branch_protection_rule', 'compare', 'name', 'prefix', 'ref_update_rule', 'repository', 'rules', 'target')
    associated_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='associatedPullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')
    compare = sgqlc.types.Field(Comparison, graphql_name='compare', args=sgqlc.types.ArgDict((
        ('head_ref', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='headRef', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    prefix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prefix')
    ref_update_rule = sgqlc.types.Field(RefUpdateRule, graphql_name='refUpdateRule')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    rules = sgqlc.types.Field(RepositoryRuleConnection, graphql_name='rules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryRuleOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )
    target = sgqlc.types.Field(GitObject, graphql_name='target')


class ReferencedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'commit', 'commit_repository', 'created_at', 'is_cross_repository', 'is_direct_reference', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    commit_repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='commitRepository')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    is_direct_reference = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirectReference')
    subject = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='subject')


class Release(sgqlc.types.Type, Node, Reactable, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('author', 'created_at', 'description', 'description_html', 'immutable', 'is_draft', 'is_latest', 'is_prerelease', 'mentions', 'name', 'published_at', 'release_assets', 'repository', 'short_description_html', 'tag', 'tag_commit', 'tag_name', 'updated_at')
    author = sgqlc.types.Field('User', graphql_name='author')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(HTML, graphql_name='descriptionHTML')
    immutable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='immutable')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_latest = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLatest')
    is_prerelease = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrerelease')
    mentions = sgqlc.types.Field(UserConnection, graphql_name='mentions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    release_assets = sgqlc.types.Field(sgqlc.types.non_null(ReleaseAssetConnection), graphql_name='releaseAssets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    short_description_html = sgqlc.types.Field(HTML, graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=200)),
))
    )
    tag = sgqlc.types.Field(Ref, graphql_name='tag')
    tag_commit = sgqlc.types.Field(Commit, graphql_name='tagCommit')
    tag_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tagName')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class ReleaseAsset(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('content_type', 'created_at', 'digest', 'download_count', 'download_url', 'name', 'release', 'size', 'updated_at', 'uploaded_by', 'url')
    content_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentType')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    digest = sgqlc.types.Field(String, graphql_name='digest')
    download_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadCount')
    download_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='downloadUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    release = sgqlc.types.Field(Release, graphql_name='release')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    uploaded_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='uploadedBy')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RemovedFromMergeQueueEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'before_commit', 'created_at', 'enqueuer', 'merge_queue', 'pull_request', 'reason')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    before_commit = sgqlc.types.Field(Commit, graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enqueuer = sgqlc.types.Field('User', graphql_name='enqueuer')
    merge_queue = sgqlc.types.Field(MergeQueue, graphql_name='mergeQueue')
    pull_request = sgqlc.types.Field(PullRequest, graphql_name='pullRequest')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class RemovedFromProjectEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class RemovedFromProjectV2Event(sgqlc.types.Type, Node, ProjectV2Event):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class RenamedTitleEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'current_title', 'previous_title', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    current_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentTitle')
    previous_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='previousTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('RenamedTitleSubject'), graphql_name='subject')


class ReopenedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'closable', 'created_at', 'state_reason')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    closable = sgqlc.types.Field(sgqlc.types.non_null(Closable), graphql_name='closable')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    state_reason = sgqlc.types.Field(IssueStateReason, graphql_name='stateReason')


class RepoAccessAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoAddMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoAddTopicAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TopicAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoArchivedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoChangeMergeSettingAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigDisableAnonymousGitAccessAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigDisableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigDisableContributorsOnlyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigDisableSockpuppetDisallowedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigEnableAnonymousGitAccessAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigEnableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigEnableContributorsOnlyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigEnableSockpuppetDisallowedAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigLockAnonymousGitAccessAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoConfigUnlockAnonymousGitAccessAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoCreateAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoDestroyAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoRemoveMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepoRemoveTopicAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TopicAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class Repository(sgqlc.types.Type, Node, PackageOwner, ProjectOwner, ProjectV2Recent, RepositoryInfo, Starrable, Subscribable, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('allow_update_branch', 'assignable_users', 'auto_merge_allowed', 'branch_protection_rules', 'code_of_conduct', 'codeowners', 'collaborators', 'commit_comments', 'contact_links', 'contributing_guidelines', 'database_id', 'default_branch_ref', 'delete_branch_on_merge', 'dependency_graph_manifests', 'deploy_keys', 'deployments', 'discussion', 'discussion_categories', 'discussion_category', 'discussions', 'disk_usage', 'environment', 'environments', 'forking_allowed', 'forks', 'funding_links', 'has_vulnerability_alerts_enabled', 'interaction_ability', 'is_blank_issues_enabled', 'is_disabled', 'is_empty', 'is_security_policy_enabled', 'is_user_configuration_repository', 'issue', 'issue_or_pull_request', 'issue_templates', 'issue_type', 'issue_types', 'issues', 'label', 'labels', 'languages', 'latest_release', 'mentionable_users', 'merge_commit_allowed', 'merge_commit_message', 'merge_commit_title', 'merge_queue', 'milestone', 'milestones', 'object', 'parent', 'pinned_discussions', 'pinned_environments', 'pinned_issues', 'plan_features', 'primary_language', 'project_v2', 'projects_resource_path', 'projects_url', 'projects_v2', 'pull_request', 'pull_request_templates', 'pull_requests', 'rebase_merge_allowed', 'ref', 'refs', 'release', 'releases', 'repository_topics', 'ruleset', 'rulesets', 'security_policy_url', 'squash_merge_allowed', 'squash_merge_commit_message', 'squash_merge_commit_title', 'ssh_url', 'submodules', 'suggested_actors', 'temp_clone_token', 'template_repository', 'viewer_can_administer', 'viewer_can_see_issue_fields', 'viewer_can_update_topics', 'viewer_default_commit_email', 'viewer_default_merge_method', 'viewer_permission', 'viewer_possible_commit_emails', 'vulnerability_alert', 'vulnerability_alerts', 'watchers', 'web_commit_signoff_required')
    allow_update_branch = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowUpdateBranch')
    assignable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignableUsers', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    auto_merge_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoMergeAllowed')
    branch_protection_rules = sgqlc.types.Field(sgqlc.types.non_null(BranchProtectionRuleConnection), graphql_name='branchProtectionRules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    code_of_conduct = sgqlc.types.Field(CodeOfConduct, graphql_name='codeOfConduct')
    codeowners = sgqlc.types.Field(RepositoryCodeowners, graphql_name='codeowners', args=sgqlc.types.ArgDict((
        ('ref_name', sgqlc.types.Arg(String, graphql_name='refName', default=None)),
))
    )
    collaborators = sgqlc.types.Field(RepositoryCollaboratorConnection, graphql_name='collaborators', args=sgqlc.types.ArgDict((
        ('affiliation', sgqlc.types.Arg(CollaboratorAffiliation, graphql_name='affiliation', default=None)),
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit_comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='commitComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    contact_links = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryContactLink)), graphql_name='contactLinks')
    contributing_guidelines = sgqlc.types.Field(ContributingGuidelines, graphql_name='contributingGuidelines')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    default_branch_ref = sgqlc.types.Field(Ref, graphql_name='defaultBranchRef')
    delete_branch_on_merge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBranchOnMerge')
    dependency_graph_manifests = sgqlc.types.Field(DependencyGraphManifestConnection, graphql_name='dependencyGraphManifests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('with_dependencies', sgqlc.types.Arg(Boolean, graphql_name='withDependencies', default=None)),
        ('dependencies_first', sgqlc.types.Arg(Int, graphql_name='dependenciesFirst', default=None)),
        ('dependencies_after', sgqlc.types.Arg(String, graphql_name='dependenciesAfter', default=None)),
))
    )
    deploy_keys = sgqlc.types.Field(sgqlc.types.non_null(DeployKeyConnection), graphql_name='deployKeys', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    deployments = sgqlc.types.Field(sgqlc.types.non_null(DeploymentConnection), graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('environments', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='environments', default=None)),
        ('order_by', sgqlc.types.Arg(DeploymentOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    discussion = sgqlc.types.Field(Discussion, graphql_name='discussion', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    discussion_categories = sgqlc.types.Field(sgqlc.types.non_null(DiscussionCategoryConnection), graphql_name='discussionCategories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('filter_by_assignable', sgqlc.types.Arg(Boolean, graphql_name='filterByAssignable', default=False)),
))
    )
    discussion_category = sgqlc.types.Field(DiscussionCategory, graphql_name='discussionCategory', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    discussions = sgqlc.types.Field(sgqlc.types.non_null(DiscussionConnection), graphql_name='discussions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('category_id', sgqlc.types.Arg(ID, graphql_name='categoryId', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(DiscussionState)), graphql_name='states', default=())),
        ('order_by', sgqlc.types.Arg(DiscussionOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('answered', sgqlc.types.Arg(Boolean, graphql_name='answered', default=None)),
))
    )
    disk_usage = sgqlc.types.Field(Int, graphql_name='diskUsage')
    environment = sgqlc.types.Field(Environment, graphql_name='environment', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    environments = sgqlc.types.Field(sgqlc.types.non_null(EnvironmentConnection), graphql_name='environments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(Environments, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
        ('pinned_environment_filter', sgqlc.types.Arg(EnvironmentPinnedFilterField, graphql_name='pinnedEnvironmentFilter', default='ALL')),
        ('names', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='names', default=())),
))
    )
    forking_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='forkingAllowed')
    forks = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='forks', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('visibility', sgqlc.types.Arg(RepositoryVisibility, graphql_name='visibility', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=('OWNER', 'COLLABORATOR'))),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('has_issues_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasIssuesEnabled', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    funding_links = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FundingLink))), graphql_name='fundingLinks')
    has_vulnerability_alerts_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasVulnerabilityAlertsEnabled')
    interaction_ability = sgqlc.types.Field(RepositoryInteractionAbility, graphql_name='interactionAbility')
    is_blank_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBlankIssuesEnabled')
    is_disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDisabled')
    is_empty = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmpty')
    is_security_policy_enabled = sgqlc.types.Field(Boolean, graphql_name='isSecurityPolicyEnabled')
    is_user_configuration_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUserConfigurationRepository')
    issue = sgqlc.types.Field(Issue, graphql_name='issue', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    issue_or_pull_request = sgqlc.types.Field('IssueOrPullRequest', graphql_name='issueOrPullRequest', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    issue_templates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueTemplate)), graphql_name='issueTemplates')
    issue_type = sgqlc.types.Field(IssueType, graphql_name='issueType', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    issue_types = sgqlc.types.Field(IssueTypeConnection, graphql_name='issueTypes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(IssueTypeOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    label = sgqlc.types.Field(Label, graphql_name='label', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(LabelOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    languages = sgqlc.types.Field(LanguageConnection, graphql_name='languages', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(LanguageOrder, graphql_name='orderBy', default=None)),
))
    )
    latest_release = sgqlc.types.Field(Release, graphql_name='latestRelease')
    mentionable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='mentionableUsers', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    merge_commit_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mergeCommitAllowed')
    merge_commit_message = sgqlc.types.Field(sgqlc.types.non_null(MergeCommitMessage), graphql_name='mergeCommitMessage')
    merge_commit_title = sgqlc.types.Field(sgqlc.types.non_null(MergeCommitTitle), graphql_name='mergeCommitTitle')
    merge_queue = sgqlc.types.Field(MergeQueue, graphql_name='mergeQueue', args=sgqlc.types.ArgDict((
        ('branch', sgqlc.types.Arg(String, graphql_name='branch', default=None)),
))
    )
    milestone = sgqlc.types.Field(Milestone, graphql_name='milestone', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    milestones = sgqlc.types.Field(MilestoneConnection, graphql_name='milestones', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(MilestoneState)), graphql_name='states', default=None)),
        ('order_by', sgqlc.types.Arg(MilestoneOrder, graphql_name='orderBy', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    object = sgqlc.types.Field(GitObject, graphql_name='object', args=sgqlc.types.ArgDict((
        ('oid', sgqlc.types.Arg(GitObjectID, graphql_name='oid', default=None)),
        ('expression', sgqlc.types.Arg(String, graphql_name='expression', default=None)),
))
    )
    parent = sgqlc.types.Field('Repository', graphql_name='parent')
    pinned_discussions = sgqlc.types.Field(sgqlc.types.non_null(PinnedDiscussionConnection), graphql_name='pinnedDiscussions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_environments = sgqlc.types.Field(PinnedEnvironmentConnection, graphql_name='pinnedEnvironments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(PinnedEnvironmentOrder, graphql_name='orderBy', default={'field': 'POSITION', 'direction': 'ASC'})),
))
    )
    pinned_issues = sgqlc.types.Field(PinnedIssueConnection, graphql_name='pinnedIssues', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    plan_features = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPlanFeatures), graphql_name='planFeatures')
    primary_language = sgqlc.types.Field(Language, graphql_name='primaryLanguage')
    project_v2 = sgqlc.types.Field(ProjectV2, graphql_name='projectV2', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    projects_v2 = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2Connection), graphql_name='projectsV2', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2Order, graphql_name='orderBy', default={'field': 'NUMBER', 'direction': 'DESC'})),
        ('min_permission_level', sgqlc.types.Arg(ProjectV2PermissionLevel, graphql_name='minPermissionLevel', default='READ')),
))
    )
    pull_request = sgqlc.types.Field(PullRequest, graphql_name='pullRequest', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    pull_request_templates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestTemplate)), graphql_name='pullRequestTemplates')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    rebase_merge_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rebaseMergeAllowed')
    ref = sgqlc.types.Field(Ref, graphql_name='ref', args=sgqlc.types.ArgDict((
        ('qualified_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='qualifiedName', default=None)),
))
    )
    refs = sgqlc.types.Field(RefConnection, graphql_name='refs', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('ref_prefix', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refPrefix', default=None)),
        ('direction', sgqlc.types.Arg(OrderDirection, graphql_name='direction', default=None)),
        ('order_by', sgqlc.types.Arg(RefOrder, graphql_name='orderBy', default=None)),
))
    )
    release = sgqlc.types.Field(Release, graphql_name='release', args=sgqlc.types.ArgDict((
        ('tag_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tagName', default=None)),
))
    )
    releases = sgqlc.types.Field(sgqlc.types.non_null(ReleaseConnection), graphql_name='releases', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ReleaseOrder, graphql_name='orderBy', default=None)),
))
    )
    repository_topics = sgqlc.types.Field(sgqlc.types.non_null(RepositoryTopicConnection), graphql_name='repositoryTopics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    ruleset = sgqlc.types.Field('RepositoryRuleset', graphql_name='ruleset', args=sgqlc.types.ArgDict((
        ('include_parents', sgqlc.types.Arg(Boolean, graphql_name='includeParents', default=True)),
        ('database_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='databaseId', default=None)),
))
    )
    rulesets = sgqlc.types.Field(RepositoryRulesetConnection, graphql_name='rulesets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_parents', sgqlc.types.Arg(Boolean, graphql_name='includeParents', default=True)),
        ('targets', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryRulesetTarget)), graphql_name='targets', default=None)),
))
    )
    security_policy_url = sgqlc.types.Field(URI, graphql_name='securityPolicyUrl')
    squash_merge_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='squashMergeAllowed')
    squash_merge_commit_message = sgqlc.types.Field(sgqlc.types.non_null(SquashMergeCommitMessage), graphql_name='squashMergeCommitMessage')
    squash_merge_commit_title = sgqlc.types.Field(sgqlc.types.non_null(SquashMergeCommitTitle), graphql_name='squashMergeCommitTitle')
    ssh_url = sgqlc.types.Field(sgqlc.types.non_null(GitSSHRemote), graphql_name='sshUrl')
    submodules = sgqlc.types.Field(sgqlc.types.non_null(SubmoduleConnection), graphql_name='submodules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    suggested_actors = sgqlc.types.Field(sgqlc.types.non_null(ActorConnection), graphql_name='suggestedActors', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('login_names', sgqlc.types.Arg(String, graphql_name='loginNames', default=None)),
        ('capabilities', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RepositorySuggestedActorFilter))), graphql_name='capabilities', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    temp_clone_token = sgqlc.types.Field(String, graphql_name='tempCloneToken')
    template_repository = sgqlc.types.Field('Repository', graphql_name='templateRepository')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_see_issue_fields = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSeeIssueFields')
    viewer_can_update_topics = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdateTopics')
    viewer_default_commit_email = sgqlc.types.Field(String, graphql_name='viewerDefaultCommitEmail')
    viewer_default_merge_method = sgqlc.types.Field(sgqlc.types.non_null(PullRequestMergeMethod), graphql_name='viewerDefaultMergeMethod')
    viewer_permission = sgqlc.types.Field(RepositoryPermission, graphql_name='viewerPermission')
    viewer_possible_commit_emails = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='viewerPossibleCommitEmails')
    vulnerability_alert = sgqlc.types.Field('RepositoryVulnerabilityAlert', graphql_name='vulnerabilityAlert', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    vulnerability_alerts = sgqlc.types.Field(RepositoryVulnerabilityAlertConnection, graphql_name='vulnerabilityAlerts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryVulnerabilityAlertState)), graphql_name='states', default=None)),
        ('dependency_scopes', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RepositoryVulnerabilityAlertDependencyScope)), graphql_name='dependencyScopes', default=None)),
))
    )
    watchers = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='watchers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    web_commit_signoff_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='webCommitSignoffRequired')


class RepositoryInvitation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('email', 'invitee', 'inviter', 'permalink', 'permission', 'repository')
    email = sgqlc.types.Field(String, graphql_name='email')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    inviter = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='inviter')
    permalink = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='permalink')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')
    repository = sgqlc.types.Field(RepositoryInfo, graphql_name='repository')


class RepositoryMigration(sgqlc.types.Type, Migration, Node):
    __schema__ = schema
    __field_names__ = ()


class RepositoryRule(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('parameters', 'repository_ruleset', 'type')
    parameters = sgqlc.types.Field('RuleParameters', graphql_name='parameters')
    repository_ruleset = sgqlc.types.Field('RepositoryRuleset', graphql_name='repositoryRuleset')
    type = sgqlc.types.Field(sgqlc.types.non_null(RepositoryRuleType), graphql_name='type')


class RepositoryRuleset(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('bypass_actors', 'conditions', 'created_at', 'database_id', 'enforcement', 'name', 'rules', 'source', 'target', 'updated_at')
    bypass_actors = sgqlc.types.Field(RepositoryRulesetBypassActorConnection, graphql_name='bypassActors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    conditions = sgqlc.types.Field(sgqlc.types.non_null(RepositoryRuleConditions), graphql_name='conditions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    enforcement = sgqlc.types.Field(sgqlc.types.non_null(RuleEnforcement), graphql_name='enforcement')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    rules = sgqlc.types.Field(RepositoryRuleConnection, graphql_name='rules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(RepositoryRuleType, graphql_name='type', default=None)),
))
    )
    source = sgqlc.types.Field(sgqlc.types.non_null('RuleSource'), graphql_name='source')
    target = sgqlc.types.Field(RepositoryRulesetTarget, graphql_name='target')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class RepositoryRulesetBypassActor(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'bypass_mode', 'deploy_key', 'enterprise_owner', 'organization_admin', 'repository_role_database_id', 'repository_role_name', 'repository_ruleset')
    actor = sgqlc.types.Field('BypassActor', graphql_name='actor')
    bypass_mode = sgqlc.types.Field(RepositoryRulesetBypassActorBypassMode, graphql_name='bypassMode')
    deploy_key = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deployKey')
    enterprise_owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enterpriseOwner')
    organization_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='organizationAdmin')
    repository_role_database_id = sgqlc.types.Field(Int, graphql_name='repositoryRoleDatabaseId')
    repository_role_name = sgqlc.types.Field(String, graphql_name='repositoryRoleName')
    repository_ruleset = sgqlc.types.Field(RepositoryRuleset, graphql_name='repositoryRuleset')


class RepositoryTopic(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('topic',)
    topic = sgqlc.types.Field(sgqlc.types.non_null('Topic'), graphql_name='topic')


class RepositoryVisibilityChangeDisableAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepositoryVisibilityChangeEnableAuditEntry(sgqlc.types.Type, AuditEntry, EnterpriseAuditEntryData, Node, OrganizationAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class RepositoryVulnerabilityAlert(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = schema
    __field_names__ = ('auto_dismissed_at', 'created_at', 'dependabot_update', 'dependency_relationship', 'dependency_scope', 'dismiss_comment', 'dismiss_reason', 'dismissed_at', 'dismisser', 'fixed_at', 'number', 'security_advisory', 'security_vulnerability', 'state', 'vulnerable_manifest_filename', 'vulnerable_manifest_path', 'vulnerable_requirements')
    auto_dismissed_at = sgqlc.types.Field(DateTime, graphql_name='autoDismissedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    dependabot_update = sgqlc.types.Field(DependabotUpdate, graphql_name='dependabotUpdate')
    dependency_relationship = sgqlc.types.Field(RepositoryVulnerabilityAlertDependencyRelationship, graphql_name='dependencyRelationship')
    dependency_scope = sgqlc.types.Field(RepositoryVulnerabilityAlertDependencyScope, graphql_name='dependencyScope')
    dismiss_comment = sgqlc.types.Field(String, graphql_name='dismissComment')
    dismiss_reason = sgqlc.types.Field(String, graphql_name='dismissReason')
    dismissed_at = sgqlc.types.Field(DateTime, graphql_name='dismissedAt')
    dismisser = sgqlc.types.Field('User', graphql_name='dismisser')
    fixed_at = sgqlc.types.Field(DateTime, graphql_name='fixedAt')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    security_advisory = sgqlc.types.Field('SecurityAdvisory', graphql_name='securityAdvisory')
    security_vulnerability = sgqlc.types.Field(SecurityVulnerability, graphql_name='securityVulnerability')
    state = sgqlc.types.Field(sgqlc.types.non_null(RepositoryVulnerabilityAlertState), graphql_name='state')
    vulnerable_manifest_filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vulnerableManifestFilename')
    vulnerable_manifest_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vulnerableManifestPath')
    vulnerable_requirements = sgqlc.types.Field(String, graphql_name='vulnerableRequirements')


class RestrictedContribution(sgqlc.types.Type, Contribution):
    __schema__ = schema
    __field_names__ = ()


class ReviewDismissalAllowance(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'branch_protection_rule')
    actor = sgqlc.types.Field('ReviewDismissalAllowanceActor', graphql_name='actor')
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')


class ReviewDismissedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'database_id', 'dismissal_message', 'dismissal_message_html', 'previous_review_state', 'pull_request', 'pull_request_commit', 'review')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    dismissal_message = sgqlc.types.Field(String, graphql_name='dismissalMessage')
    dismissal_message_html = sgqlc.types.Field(String, graphql_name='dismissalMessageHTML')
    previous_review_state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='previousReviewState')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    pull_request_commit = sgqlc.types.Field(PullRequestCommit, graphql_name='pullRequestCommit')
    review = sgqlc.types.Field(PullRequestReview, graphql_name='review')


class ReviewRequest(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('as_code_owner', 'database_id', 'pull_request', 'requested_reviewer')
    as_code_owner = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='asCodeOwner')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewRequestRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'pull_request', 'requested_reviewer')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewRequestedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'pull_request', 'requested_reviewer')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewStatusHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = schema
    __field_names__ = ('review_decision',)
    review_decision = sgqlc.types.Field(PullRequestReviewDecision, graphql_name='reviewDecision')


class SavedReply(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('body', 'body_html', 'database_id', 'title', 'user')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    user = sgqlc.types.Field(Actor, graphql_name='user')


class SecurityAdvisory(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('classification', 'cvss_severities', 'cwes', 'database_id', 'description', 'epss', 'ghsa_id', 'identifiers', 'notifications_permalink', 'origin', 'permalink', 'published_at', 'references', 'severity', 'summary', 'updated_at', 'vulnerabilities', 'withdrawn_at')
    classification = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryClassification), graphql_name='classification')
    cvss_severities = sgqlc.types.Field(sgqlc.types.non_null(CvssSeverities), graphql_name='cvssSeverities')
    cwes = sgqlc.types.Field(sgqlc.types.non_null(CWEConnection), graphql_name='cwes', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    epss = sgqlc.types.Field(EPSS, graphql_name='epss')
    ghsa_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ghsaId')
    identifiers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryIdentifier))), graphql_name='identifiers')
    notifications_permalink = sgqlc.types.Field(URI, graphql_name='notificationsPermalink')
    origin = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='origin')
    permalink = sgqlc.types.Field(URI, graphql_name='permalink')
    published_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='publishedAt')
    references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryReference))), graphql_name='references')
    severity = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisorySeverity), graphql_name='severity')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    vulnerabilities = sgqlc.types.Field(sgqlc.types.non_null(SecurityVulnerabilityConnection), graphql_name='vulnerabilities', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(SecurityVulnerabilityOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('ecosystem', sgqlc.types.Arg(SecurityAdvisoryEcosystem, graphql_name='ecosystem', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('severities', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisorySeverity)), graphql_name='severities', default=None)),
        ('classifications', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryClassification)), graphql_name='classifications', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    withdrawn_at = sgqlc.types.Field(DateTime, graphql_name='withdrawnAt')


class SmimeSignature(sgqlc.types.Type, GitSignature):
    __schema__ = schema
    __field_names__ = ()


class SponsorsActivity(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('action', 'current_privacy_level', 'payment_source', 'previous_sponsors_tier', 'sponsor', 'sponsorable', 'sponsors_tier', 'timestamp', 'via_bulk_sponsorship')
    action = sgqlc.types.Field(sgqlc.types.non_null(SponsorsActivityAction), graphql_name='action')
    current_privacy_level = sgqlc.types.Field(SponsorshipPrivacy, graphql_name='currentPrivacyLevel')
    payment_source = sgqlc.types.Field(SponsorshipPaymentSource, graphql_name='paymentSource')
    previous_sponsors_tier = sgqlc.types.Field('SponsorsTier', graphql_name='previousSponsorsTier')
    sponsor = sgqlc.types.Field('Sponsor', graphql_name='sponsor')
    sponsorable = sgqlc.types.Field(sgqlc.types.non_null(Sponsorable), graphql_name='sponsorable')
    sponsors_tier = sgqlc.types.Field('SponsorsTier', graphql_name='sponsorsTier')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    via_bulk_sponsorship = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viaBulkSponsorship')


class SponsorsListing(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('active_goal', 'active_stripe_connect_account', 'billing_country_or_region', 'contact_email_address', 'created_at', 'dashboard_resource_path', 'dashboard_url', 'featured_items', 'fiscal_host', 'full_description', 'full_description_html', 'is_public', 'name', 'next_payout_date', 'residence_country_or_region', 'resource_path', 'short_description', 'slug', 'sponsorable', 'tiers', 'url')
    active_goal = sgqlc.types.Field(SponsorsGoal, graphql_name='activeGoal')
    active_stripe_connect_account = sgqlc.types.Field(StripeConnectAccount, graphql_name='activeStripeConnectAccount')
    billing_country_or_region = sgqlc.types.Field(String, graphql_name='billingCountryOrRegion')
    contact_email_address = sgqlc.types.Field(String, graphql_name='contactEmailAddress')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    dashboard_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='dashboardResourcePath')
    dashboard_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='dashboardUrl')
    featured_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SponsorsListingFeaturedItem'))), graphql_name='featuredItems', args=sgqlc.types.ArgDict((
        ('featureable_types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SponsorsListingFeaturedItemFeatureableType)), graphql_name='featureableTypes', default=('REPOSITORY', 'USER'))),
))
    )
    fiscal_host = sgqlc.types.Field(Organization, graphql_name='fiscalHost')
    full_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullDescription')
    full_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='fullDescriptionHTML')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    next_payout_date = sgqlc.types.Field(Date, graphql_name='nextPayoutDate')
    residence_country_or_region = sgqlc.types.Field(String, graphql_name='residenceCountryOrRegion')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortDescription')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    sponsorable = sgqlc.types.Field(sgqlc.types.non_null(Sponsorable), graphql_name='sponsorable')
    tiers = sgqlc.types.Field(SponsorsTierConnection, graphql_name='tiers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorsTierOrder, graphql_name='orderBy', default={'field': 'MONTHLY_PRICE_IN_CENTS', 'direction': 'ASC'})),
        ('include_unpublished', sgqlc.types.Arg(Boolean, graphql_name='includeUnpublished', default=False)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class SponsorsListingFeaturedItem(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'description', 'featureable', 'position', 'sponsors_listing', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    featureable = sgqlc.types.Field(sgqlc.types.non_null('SponsorsListingFeatureableItem'), graphql_name='featureable')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    sponsors_listing = sgqlc.types.Field(sgqlc.types.non_null(SponsorsListing), graphql_name='sponsorsListing')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class SponsorsTier(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('admin_info', 'closest_lesser_value_tier', 'created_at', 'description', 'description_html', 'is_custom_amount', 'is_one_time', 'monthly_price_in_cents', 'monthly_price_in_dollars', 'name', 'sponsors_listing', 'updated_at')
    admin_info = sgqlc.types.Field(SponsorsTierAdminInfo, graphql_name='adminInfo')
    closest_lesser_value_tier = sgqlc.types.Field('SponsorsTier', graphql_name='closestLesserValueTier')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    is_custom_amount = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCustomAmount')
    is_one_time = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOneTime')
    monthly_price_in_cents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='monthlyPriceInCents')
    monthly_price_in_dollars = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='monthlyPriceInDollars')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    sponsors_listing = sgqlc.types.Field(sgqlc.types.non_null(SponsorsListing), graphql_name='sponsorsListing')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Sponsorship(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'is_active', 'is_one_time_payment', 'is_sponsor_opted_into_email', 'payment_source', 'privacy_level', 'sponsor_entity', 'sponsorable', 'tier', 'tier_selected_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    is_one_time_payment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOneTimePayment')
    is_sponsor_opted_into_email = sgqlc.types.Field(Boolean, graphql_name='isSponsorOptedIntoEmail')
    payment_source = sgqlc.types.Field(SponsorshipPaymentSource, graphql_name='paymentSource')
    privacy_level = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipPrivacy), graphql_name='privacyLevel')
    sponsor_entity = sgqlc.types.Field('Sponsor', graphql_name='sponsorEntity')
    sponsorable = sgqlc.types.Field(sgqlc.types.non_null(Sponsorable), graphql_name='sponsorable')
    tier = sgqlc.types.Field(SponsorsTier, graphql_name='tier')
    tier_selected_at = sgqlc.types.Field(DateTime, graphql_name='tierSelectedAt')


class SponsorshipNewsletter(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('author', 'body', 'created_at', 'is_published', 'sponsorable', 'subject', 'updated_at')
    author = sgqlc.types.Field('User', graphql_name='author')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    sponsorable = sgqlc.types.Field(sgqlc.types.non_null(Sponsorable), graphql_name='sponsorable')
    subject = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subject')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class SshSignature(sgqlc.types.Type, GitSignature):
    __schema__ = schema
    __field_names__ = ('key_fingerprint',)
    key_fingerprint = sgqlc.types.Field(String, graphql_name='keyFingerprint')


class Status(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('combined_contexts', 'commit', 'context', 'contexts', 'state')
    combined_contexts = sgqlc.types.Field(sgqlc.types.non_null(StatusCheckRollupContextConnection), graphql_name='combinedContexts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    context = sgqlc.types.Field('StatusContext', graphql_name='context', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    contexts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatusContext'))), graphql_name='contexts')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')


class StatusCheckRollup(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('commit', 'contexts', 'state')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    contexts = sgqlc.types.Field(sgqlc.types.non_null(StatusCheckRollupContextConnection), graphql_name='contexts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')


class StatusContext(sgqlc.types.Type, Node, RequirableByPullRequest):
    __schema__ = schema
    __field_names__ = ('avatar_url', 'commit', 'context', 'created_at', 'creator', 'description', 'state', 'target_url')
    avatar_url = sgqlc.types.Field(URI, graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=40)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')
    target_url = sgqlc.types.Field(URI, graphql_name='targetUrl')


class SubIssueAddedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'sub_issue')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    sub_issue = sgqlc.types.Field(Issue, graphql_name='subIssue')


class SubIssueRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'sub_issue')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    sub_issue = sgqlc.types.Field(Issue, graphql_name='subIssue')


class SubscribedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'subscribable')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class Tag(sgqlc.types.Type, GitObject, Node):
    __schema__ = schema
    __field_names__ = ('message', 'name', 'tagger', 'target')
    message = sgqlc.types.Field(String, graphql_name='message')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    tagger = sgqlc.types.Field(GitActor, graphql_name='tagger')
    target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='target')


class Team(sgqlc.types.Type, MemberStatusable, Node, Subscribable):
    __schema__ = schema
    __field_names__ = ('ancestors', 'avatar_url', 'child_teams', 'combined_slug', 'created_at', 'database_id', 'description', 'discussion', 'discussions', 'discussions_resource_path', 'discussions_url', 'edit_team_resource_path', 'edit_team_url', 'invitations', 'members', 'members_resource_path', 'members_url', 'name', 'new_team_resource_path', 'new_team_url', 'notification_setting', 'organization', 'parent_team', 'privacy', 'project_v2', 'projects_v2', 'repositories', 'repositories_resource_path', 'repositories_url', 'resource_path', 'review_request_delegation_algorithm', 'review_request_delegation_enabled', 'review_request_delegation_member_count', 'review_request_delegation_notify_team', 'slug', 'teams_resource_path', 'teams_url', 'updated_at', 'url', 'viewer_can_administer')
    ancestors = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    avatar_url = sgqlc.types.Field(URI, graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=400)),
))
    )
    child_teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='childTeams', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default=None)),
        ('user_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userLogins', default=None)),
        ('immediate_only', sgqlc.types.Arg(Boolean, graphql_name='immediateOnly', default=True)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    combined_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='combinedSlug')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    discussion = sgqlc.types.Field('TeamDiscussion', graphql_name='discussion', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    discussions = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionConnection), graphql_name='discussions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_pinned', sgqlc.types.Arg(Boolean, graphql_name='isPinned', default=None)),
        ('order_by', sgqlc.types.Arg(TeamDiscussionOrder, graphql_name='orderBy', default=None)),
))
    )
    discussions_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='discussionsResourcePath')
    discussions_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='discussionsUrl')
    edit_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='editTeamResourcePath')
    edit_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='editTeamUrl')
    invitations = sgqlc.types.Field(OrganizationInvitationConnection, graphql_name='invitations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    members = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('membership', sgqlc.types.Arg(TeamMembershipType, graphql_name='membership', default='ALL')),
        ('role', sgqlc.types.Arg(TeamMemberRole, graphql_name='role', default=None)),
        ('order_by', sgqlc.types.Arg(TeamMemberOrder, graphql_name='orderBy', default=None)),
))
    )
    members_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='membersResourcePath')
    members_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='membersUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    new_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamResourcePath')
    new_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamUrl')
    notification_setting = sgqlc.types.Field(sgqlc.types.non_null(TeamNotificationSetting), graphql_name='notificationSetting')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    parent_team = sgqlc.types.Field('Team', graphql_name='parentTeam')
    privacy = sgqlc.types.Field(sgqlc.types.non_null(TeamPrivacy), graphql_name='privacy')
    project_v2 = sgqlc.types.Field(ProjectV2, graphql_name='projectV2', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects_v2 = sgqlc.types.Field(sgqlc.types.non_null(ProjectV2Connection), graphql_name='projectsV2', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectV2Order, graphql_name='orderBy', default={'field': 'NUMBER', 'direction': 'DESC'})),
        ('filter_by', sgqlc.types.Arg(ProjectV2Filters, graphql_name='filterBy', default={})),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default='')),
        ('min_permission_level', sgqlc.types.Arg(ProjectV2PermissionLevel, graphql_name='minPermissionLevel', default='READ')),
))
    )
    repositories = sgqlc.types.Field(sgqlc.types.non_null(TeamRepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(TeamRepositoryOrder, graphql_name='orderBy', default=None)),
))
    )
    repositories_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoriesResourcePath')
    repositories_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoriesUrl')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    review_request_delegation_algorithm = sgqlc.types.Field(TeamReviewAssignmentAlgorithm, graphql_name='reviewRequestDelegationAlgorithm')
    review_request_delegation_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewRequestDelegationEnabled')
    review_request_delegation_member_count = sgqlc.types.Field(Int, graphql_name='reviewRequestDelegationMemberCount')
    review_request_delegation_notify_team = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewRequestDelegationNotifyTeam')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')


class TeamAddMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, TeamAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class TeamAddRepositoryAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TeamAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class TeamChangeParentTeamAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, TeamAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class TeamDiscussion(sgqlc.types.Type, Comment, Deletable, Node, Reactable, Subscribable, UniformResourceLocatable, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ()


class TeamDiscussionComment(sgqlc.types.Type, Comment, Deletable, Node, Reactable, UniformResourceLocatable, Updatable, UpdatableComment):
    __schema__ = schema
    __field_names__ = ()


class TeamRemoveMemberAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, TeamAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class TeamRemoveRepositoryAuditEntry(sgqlc.types.Type, AuditEntry, Node, OrganizationAuditEntryData, RepositoryAuditEntryData, TeamAuditEntryData):
    __schema__ = schema
    __field_names__ = ()


class Topic(sgqlc.types.Type, Node, Starrable):
    __schema__ = schema
    __field_names__ = ('name', 'related_topics', 'repositories')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    related_topics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Topic'))), graphql_name='relatedTopics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=3)),
))
    )
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('visibility', sgqlc.types.Arg(RepositoryVisibility, graphql_name='visibility', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=('OWNER', 'COLLABORATOR'))),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('has_issues_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasIssuesEnabled', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('sponsorable_only', sgqlc.types.Arg(Boolean, graphql_name='sponsorableOnly', default=False)),
))
    )


class TransferredEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'from_repository', 'issue')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    from_repository = sgqlc.types.Field(Repository, graphql_name='fromRepository')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')


class Tree(sgqlc.types.Type, GitObject, Node):
    __schema__ = schema
    __field_names__ = ('entries',)
    entries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TreeEntry)), graphql_name='entries')


class UnassignedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'assignable', 'assignee', 'created_at')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    assignable = sgqlc.types.Field(sgqlc.types.non_null(Assignable), graphql_name='assignable')
    assignee = sgqlc.types.Field('Assignee', graphql_name='assignee')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')


class UnknownSignature(sgqlc.types.Type, GitSignature):
    __schema__ = schema
    __field_names__ = ()


class UnlabeledEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'label', 'labelable')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    label = sgqlc.types.Field(sgqlc.types.non_null(Label), graphql_name='label')
    labelable = sgqlc.types.Field(sgqlc.types.non_null(Labelable), graphql_name='labelable')


class UnlockedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'lockable')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    lockable = sgqlc.types.Field(sgqlc.types.non_null(Lockable), graphql_name='lockable')


class UnmarkedAsDuplicateEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'canonical', 'created_at', 'duplicate', 'is_cross_repository')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    canonical = sgqlc.types.Field('IssueOrPullRequest', graphql_name='canonical')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    duplicate = sgqlc.types.Field('IssueOrPullRequest', graphql_name='duplicate')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')


class UnpinnedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'issue')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')


class UnsubscribedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'created_at', 'subscribable')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class User(sgqlc.types.Type, Actor, Node, PackageOwner, ProfileOwner, ProjectOwner, ProjectV2Owner, ProjectV2Recent, RepositoryDiscussionAuthor, RepositoryDiscussionCommentAuthor, RepositoryOwner, Sponsorable, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('bio', 'bio_html', 'can_receive_organization_emails_when_notifications_restricted', 'commit_comments', 'company', 'company_html', 'contributions_collection', 'copilot_endpoints', 'created_at', 'database_id', 'enterprises', 'followers', 'following', 'gist', 'gist_comments', 'gists', 'hovercard', 'interaction_ability', 'is_bounty_hunter', 'is_campus_expert', 'is_developer_program_member', 'is_employee', 'is_following_viewer', 'is_git_hub_star', 'is_hireable', 'is_site_admin', 'is_viewer', 'issue_comments', 'issues', 'lists', 'organization', 'organization_verified_domain_emails', 'organizations', 'projects_resource_path', 'projects_url', 'pronouns', 'public_keys', 'pull_requests', 'repositories_contributed_to', 'saved_replies', 'social_accounts', 'starred_repositories', 'status', 'suggested_list_names', 'top_repositories', 'twitter_username', 'updated_at', 'user_view_type', 'viewer_can_follow', 'viewer_is_following', 'watching')
    bio = sgqlc.types.Field(String, graphql_name='bio')
    bio_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bioHTML')
    can_receive_organization_emails_when_notifications_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canReceiveOrganizationEmailsWhenNotificationsRestricted', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    commit_comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='commitComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    company = sgqlc.types.Field(String, graphql_name='company')
    company_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='companyHTML')
    contributions_collection = sgqlc.types.Field(sgqlc.types.non_null(ContributionsCollection), graphql_name='contributionsCollection', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('from_', sgqlc.types.Arg(DateTime, graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(DateTime, graphql_name='to', default=None)),
))
    )
    copilot_endpoints = sgqlc.types.Field(CopilotEndpoints, graphql_name='copilotEndpoints')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    enterprises = sgqlc.types.Field(EnterpriseConnection, graphql_name='enterprises', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
        ('membership_type', sgqlc.types.Arg(EnterpriseMembershipType, graphql_name='membershipType', default='ALL')),
))
    )
    followers = sgqlc.types.Field(sgqlc.types.non_null(FollowerConnection), graphql_name='followers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    following = sgqlc.types.Field(sgqlc.types.non_null(FollowingConnection), graphql_name='following', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    gist = sgqlc.types.Field(Gist, graphql_name='gist', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    gist_comments = sgqlc.types.Field(sgqlc.types.non_null(GistCommentConnection), graphql_name='gistComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    gists = sgqlc.types.Field(sgqlc.types.non_null(GistConnection), graphql_name='gists', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(GistPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(GistOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    hovercard = sgqlc.types.Field(sgqlc.types.non_null(Hovercard), graphql_name='hovercard', args=sgqlc.types.ArgDict((
        ('primary_subject_id', sgqlc.types.Arg(ID, graphql_name='primarySubjectId', default=None)),
))
    )
    interaction_ability = sgqlc.types.Field(RepositoryInteractionAbility, graphql_name='interactionAbility')
    is_bounty_hunter = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBountyHunter')
    is_campus_expert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCampusExpert')
    is_developer_program_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeveloperProgramMember')
    is_employee = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmployee')
    is_following_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFollowingViewer')
    is_git_hub_star = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGitHubStar')
    is_hireable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHireable')
    is_site_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSiteAdmin')
    is_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isViewer')
    issue_comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='issueComments', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueCommentOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    lists = sgqlc.types.Field(sgqlc.types.non_null(UserListConnection), graphql_name='lists', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    organization = sgqlc.types.Field(Organization, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    organization_verified_domain_emails = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='organizationVerifiedDomainEmails', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    pronouns = sgqlc.types.Field(String, graphql_name='pronouns')
    public_keys = sgqlc.types.Field(sgqlc.types.non_null(PublicKeyConnection), graphql_name='publicKeys', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repositories_contributed_to = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositoriesContributedTo', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('has_issues', sgqlc.types.Arg(Boolean, graphql_name='hasIssues', default=None)),
        ('include_user_repositories', sgqlc.types.Arg(Boolean, graphql_name='includeUserRepositories', default=None)),
        ('contribution_types', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryContributionType), graphql_name='contributionTypes', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    saved_replies = sgqlc.types.Field(SavedReplyConnection, graphql_name='savedReplies', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SavedReplyOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )
    social_accounts = sgqlc.types.Field(sgqlc.types.non_null(SocialAccountConnection), graphql_name='socialAccounts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    starred_repositories = sgqlc.types.Field(sgqlc.types.non_null(StarredRepositoryConnection), graphql_name='starredRepositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('owned_by_viewer', sgqlc.types.Arg(Boolean, graphql_name='ownedByViewer', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    status = sgqlc.types.Field('UserStatus', graphql_name='status')
    suggested_list_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserListSuggestion))), graphql_name='suggestedListNames')
    top_repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='topRepositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.non_null(RepositoryOrder), graphql_name='orderBy', default=None)),
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
))
    )
    twitter_username = sgqlc.types.Field(String, graphql_name='twitterUsername')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_view_type = sgqlc.types.Field(sgqlc.types.non_null(UserViewType), graphql_name='userViewType')
    viewer_can_follow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanFollow')
    viewer_is_following = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsFollowing')
    watching = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='watching', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('visibility', sgqlc.types.Arg(RepositoryVisibility, graphql_name='visibility', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=('OWNER', 'COLLABORATOR'))),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('has_issues_enabled', sgqlc.types.Arg(Boolean, graphql_name='hasIssuesEnabled', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class UserBlockedEvent(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('actor', 'block_duration', 'created_at', 'subject')
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    block_duration = sgqlc.types.Field(sgqlc.types.non_null(UserBlockDuration), graphql_name='blockDuration')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    subject = sgqlc.types.Field(User, graphql_name='subject')


class UserContentEdit(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'deleted_at', 'deleted_by', 'diff', 'edited_at', 'editor', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    deleted_at = sgqlc.types.Field(DateTime, graphql_name='deletedAt')
    deleted_by = sgqlc.types.Field(Actor, graphql_name='deletedBy')
    diff = sgqlc.types.Field(String, graphql_name='diff')
    edited_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='editedAt')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class UserList(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'description', 'is_private', 'items', 'last_added_at', 'name', 'slug', 'updated_at', 'user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    items = sgqlc.types.Field(sgqlc.types.non_null(UserListItemsConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    last_added_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastAddedAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')


class UserNamespaceRepository(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('name', 'name_with_owner', 'owner')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    owner = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOwner), graphql_name='owner')


class UserStatus(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'emoji', 'emoji_html', 'expires_at', 'indicates_limited_availability', 'message', 'organization', 'updated_at', 'user')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    emoji = sgqlc.types.Field(String, graphql_name='emoji')
    emoji_html = sgqlc.types.Field(HTML, graphql_name='emojiHTML')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    indicates_limited_availability = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='indicatesLimitedAvailability')
    message = sgqlc.types.Field(String, graphql_name='message')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')


class VerifiableDomain(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_at', 'database_id', 'dns_host_name', 'domain', 'has_found_host_name', 'has_found_verification_token', 'is_approved', 'is_required_for_policy_enforcement', 'is_verified', 'owner', 'punycode_encoded_domain', 'token_expiration_time', 'updated_at', 'verification_token')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    dns_host_name = sgqlc.types.Field(URI, graphql_name='dnsHostName')
    domain = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='domain')
    has_found_host_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasFoundHostName')
    has_found_verification_token = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasFoundVerificationToken')
    is_approved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproved')
    is_required_for_policy_enforcement = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequiredForPolicyEnforcement')
    is_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerified')
    owner = sgqlc.types.Field(sgqlc.types.non_null('VerifiableDomainOwner'), graphql_name='owner')
    punycode_encoded_domain = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='punycodeEncodedDomain')
    token_expiration_time = sgqlc.types.Field(DateTime, graphql_name='tokenExpirationTime')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    verification_token = sgqlc.types.Field(String, graphql_name='verificationToken')


class ViewerHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = schema
    __field_names__ = ('viewer',)
    viewer = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='viewer')


class Workflow(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('created_at', 'database_id', 'name', 'runs', 'state', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    runs = sgqlc.types.Field(sgqlc.types.non_null(WorkflowRunConnection), graphql_name='runs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(WorkflowRunOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(WorkflowState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class WorkflowRun(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('check_suite', 'created_at', 'database_id', 'deployment_reviews', 'event', 'file', 'pending_deployment_requests', 'run_number', 'updated_at', 'workflow')
    check_suite = sgqlc.types.Field(sgqlc.types.non_null(CheckSuite), graphql_name='checkSuite')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    deployment_reviews = sgqlc.types.Field(sgqlc.types.non_null(DeploymentReviewConnection), graphql_name='deploymentReviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='event')
    file = sgqlc.types.Field('WorkflowRunFile', graphql_name='file')
    pending_deployment_requests = sgqlc.types.Field(sgqlc.types.non_null(DeploymentRequestConnection), graphql_name='pendingDeploymentRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    run_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='runNumber')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    workflow = sgqlc.types.Field(sgqlc.types.non_null(Workflow), graphql_name='workflow')


class WorkflowRunFile(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = schema
    __field_names__ = ('path', 'repository_file_url', 'repository_name', 'run', 'viewer_can_push_repository', 'viewer_can_read_repository')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    repository_file_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoryFileUrl')
    repository_name = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoryName')
    run = sgqlc.types.Field(sgqlc.types.non_null(WorkflowRun), graphql_name='run')
    viewer_can_push_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanPushRepository')
    viewer_can_read_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReadRepository')



########################################################################
# Unions
########################################################################
class Assignee(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Bot, Mannequin, Organization, User)


class AuditEntryActor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Bot, Organization, User)


class BranchActorAllowanceActor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (App, Team, User)


class BypassActor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (App, Team)


class Claimable(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Mannequin, User)


class Closer(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Commit, ProjectV2, PullRequest)


class CreatedIssueOrRestrictedContribution(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (CreatedIssueContribution, RestrictedContribution)


class CreatedPullRequestOrRestrictedContribution(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (CreatedPullRequestContribution, RestrictedContribution)


class CreatedRepositoryOrRestrictedContribution(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (CreatedRepositoryContribution, RestrictedContribution)


class DeploymentReviewer(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Team, User)


class EnterpriseMember(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (EnterpriseUserAccount, User)


class IpAllowListOwner(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (App, Enterprise, Organization)


class IssueOrPullRequest(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Issue, PullRequest)


class IssueTimelineItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (AssignedEvent, ClosedEvent, Commit, CrossReferencedEvent, DemilestonedEvent, IssueComment, LabeledEvent, LockedEvent, MilestonedEvent, ReferencedEvent, RenamedTitleEvent, ReopenedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UnsubscribedEvent, UserBlockedEvent)


class IssueTimelineItems(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (AddedToProjectEvent, AddedToProjectV2Event, AssignedEvent, BlockedByAddedEvent, BlockedByRemovedEvent, BlockingAddedEvent, BlockingRemovedEvent, ClosedEvent, CommentDeletedEvent, ConnectedEvent, ConvertedFromDraftEvent, ConvertedNoteToIssueEvent, ConvertedToDiscussionEvent, CrossReferencedEvent, DemilestonedEvent, DisconnectedEvent, IssueComment, IssueTypeAddedEvent, IssueTypeChangedEvent, IssueTypeRemovedEvent, LabeledEvent, LockedEvent, MarkedAsDuplicateEvent, MentionedEvent, MilestonedEvent, MovedColumnsInProjectEvent, ParentIssueAddedEvent, ParentIssueRemovedEvent, PinnedEvent, ProjectV2ItemStatusChangedEvent, ReferencedEvent, RemovedFromProjectEvent, RemovedFromProjectV2Event, RenamedTitleEvent, ReopenedEvent, SubIssueAddedEvent, SubIssueRemovedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UnmarkedAsDuplicateEvent, UnpinnedEvent, UnsubscribedEvent, UserBlockedEvent)


class MilestoneItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Issue, PullRequest)


class OrgRestoreMemberAuditEntryMembership(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (OrgRestoreMemberMembershipOrganizationAuditEntryData, OrgRestoreMemberMembershipRepositoryAuditEntryData, OrgRestoreMemberMembershipTeamAuditEntryData)


class OrganizationAuditEntry(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (MembersCanDeleteReposClearAuditEntry, MembersCanDeleteReposDisableAuditEntry, MembersCanDeleteReposEnableAuditEntry, OauthApplicationCreateAuditEntry, OrgAddBillingManagerAuditEntry, OrgAddMemberAuditEntry, OrgBlockUserAuditEntry, OrgConfigDisableCollaboratorsOnlyAuditEntry, OrgConfigEnableCollaboratorsOnlyAuditEntry, OrgCreateAuditEntry, OrgDisableOauthAppRestrictionsAuditEntry, OrgDisableSamlAuditEntry, OrgDisableTwoFactorRequirementAuditEntry, OrgEnableOauthAppRestrictionsAuditEntry, OrgEnableSamlAuditEntry, OrgEnableTwoFactorRequirementAuditEntry, OrgInviteMemberAuditEntry, OrgInviteToBusinessAuditEntry, OrgOauthAppAccessApprovedAuditEntry, OrgOauthAppAccessBlockedAuditEntry, OrgOauthAppAccessDeniedAuditEntry, OrgOauthAppAccessRequestedAuditEntry, OrgOauthAppAccessUnblockedAuditEntry, OrgRemoveBillingManagerAuditEntry, OrgRemoveMemberAuditEntry, OrgRemoveOutsideCollaboratorAuditEntry, OrgRestoreMemberAuditEntry, OrgUnblockUserAuditEntry, OrgUpdateDefaultRepositoryPermissionAuditEntry, OrgUpdateMemberAuditEntry, OrgUpdateMemberRepositoryCreationPermissionAuditEntry, OrgUpdateMemberRepositoryInvitationPermissionAuditEntry, PrivateRepositoryForkingDisableAuditEntry, PrivateRepositoryForkingEnableAuditEntry, RepoAccessAuditEntry, RepoAddMemberAuditEntry, RepoAddTopicAuditEntry, RepoArchivedAuditEntry, RepoChangeMergeSettingAuditEntry, RepoConfigDisableAnonymousGitAccessAuditEntry, RepoConfigDisableCollaboratorsOnlyAuditEntry, RepoConfigDisableContributorsOnlyAuditEntry, RepoConfigDisableSockpuppetDisallowedAuditEntry, RepoConfigEnableAnonymousGitAccessAuditEntry, RepoConfigEnableCollaboratorsOnlyAuditEntry, RepoConfigEnableContributorsOnlyAuditEntry, RepoConfigEnableSockpuppetDisallowedAuditEntry, RepoConfigLockAnonymousGitAccessAuditEntry, RepoConfigUnlockAnonymousGitAccessAuditEntry, RepoCreateAuditEntry, RepoDestroyAuditEntry, RepoRemoveMemberAuditEntry, RepoRemoveTopicAuditEntry, RepositoryVisibilityChangeDisableAuditEntry, RepositoryVisibilityChangeEnableAuditEntry, TeamAddMemberAuditEntry, TeamAddRepositoryAuditEntry, TeamChangeParentTeamAuditEntry, TeamRemoveMemberAuditEntry, TeamRemoveRepositoryAuditEntry)


class OrganizationOrUser(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Organization, User)


class PermissionGranter(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Organization, Repository, Team)


class PinnableItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Gist, Repository)


class ProjectCardItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Issue, PullRequest)


class ProjectV2Actor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Team, User)


class ProjectV2FieldConfiguration(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (ProjectV2Field, ProjectV2IterationField, ProjectV2SingleSelectField)


class ProjectV2ItemContent(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (DraftIssue, Issue, PullRequest)


class ProjectV2ItemFieldValue(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (ProjectV2ItemFieldDateValue, ProjectV2ItemFieldIterationValue, ProjectV2ItemFieldLabelValue, ProjectV2ItemFieldMilestoneValue, ProjectV2ItemFieldNumberValue, ProjectV2ItemFieldPullRequestValue, ProjectV2ItemFieldRepositoryValue, ProjectV2ItemFieldReviewerValue, ProjectV2ItemFieldSingleSelectValue, ProjectV2ItemFieldTextValue, ProjectV2ItemFieldUserValue)


class PullRequestTimelineItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (AssignedEvent, BaseRefDeletedEvent, BaseRefForcePushedEvent, ClosedEvent, Commit, CommitCommentThread, CrossReferencedEvent, DemilestonedEvent, DeployedEvent, DeploymentEnvironmentChangedEvent, HeadRefDeletedEvent, HeadRefForcePushedEvent, HeadRefRestoredEvent, IssueComment, LabeledEvent, LockedEvent, MergedEvent, MilestonedEvent, PullRequestReview, PullRequestReviewComment, PullRequestReviewThread, ReferencedEvent, RenamedTitleEvent, ReopenedEvent, ReviewDismissedEvent, ReviewRequestRemovedEvent, ReviewRequestedEvent, SubscribedEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UnsubscribedEvent, UserBlockedEvent)


class PullRequestTimelineItems(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (AddedToMergeQueueEvent, AddedToProjectEvent, AddedToProjectV2Event, AssignedEvent, AutoMergeDisabledEvent, AutoMergeEnabledEvent, AutoRebaseEnabledEvent, AutoSquashEnabledEvent, AutomaticBaseChangeFailedEvent, AutomaticBaseChangeSucceededEvent, BaseRefChangedEvent, BaseRefDeletedEvent, BaseRefForcePushedEvent, BlockedByAddedEvent, BlockedByRemovedEvent, BlockingAddedEvent, BlockingRemovedEvent, ClosedEvent, CommentDeletedEvent, ConnectedEvent, ConvertToDraftEvent, ConvertedFromDraftEvent, ConvertedNoteToIssueEvent, ConvertedToDiscussionEvent, CrossReferencedEvent, DemilestonedEvent, DeployedEvent, DeploymentEnvironmentChangedEvent, DisconnectedEvent, HeadRefDeletedEvent, HeadRefForcePushedEvent, HeadRefRestoredEvent, IssueComment, IssueTypeAddedEvent, IssueTypeChangedEvent, IssueTypeRemovedEvent, LabeledEvent, LockedEvent, MarkedAsDuplicateEvent, MentionedEvent, MergedEvent, MilestonedEvent, MovedColumnsInProjectEvent, ParentIssueAddedEvent, ParentIssueRemovedEvent, PinnedEvent, ProjectV2ItemStatusChangedEvent, PullRequestCommit, PullRequestCommitCommentThread, PullRequestReview, PullRequestReviewThread, PullRequestRevisionMarker, ReadyForReviewEvent, ReferencedEvent, RemovedFromMergeQueueEvent, RemovedFromProjectEvent, RemovedFromProjectV2Event, RenamedTitleEvent, ReopenedEvent, ReviewDismissedEvent, ReviewRequestRemovedEvent, ReviewRequestedEvent, SubIssueAddedEvent, SubIssueRemovedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UnmarkedAsDuplicateEvent, UnpinnedEvent, UnsubscribedEvent, UserBlockedEvent)


class PushAllowanceActor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (App, Team, User)


class Reactor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Bot, Mannequin, Organization, User)


class ReferencedSubject(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Issue, PullRequest)


class RenamedTitleSubject(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Issue, PullRequest)


class RequestedReviewer(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Bot, Mannequin, Team, User)


class ReviewDismissalAllowanceActor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (App, Team, User)


class RuleParameters(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (BranchNamePatternParameters, CodeScanningParameters, CommitAuthorEmailPatternParameters, CommitMessagePatternParameters, CommitterEmailPatternParameters, CopilotCodeReviewParameters, FileExtensionRestrictionParameters, FilePathRestrictionParameters, MaxFilePathLengthParameters, MaxFileSizeParameters, MergeQueueParameters, PullRequestParameters, RequiredDeploymentsParameters, RequiredStatusChecksParameters, TagNamePatternParameters, UpdateParameters, WorkflowsParameters)


class RuleSource(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Enterprise, Organization, Repository)


class SearchResultItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (App, Discussion, Issue, MarketplaceListing, Organization, PullRequest, Repository, User)


class Sponsor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Organization, User)


class SponsorableItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Organization, User)


class SponsorsListingFeatureableItem(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Repository, User)


class StatusCheckRollupContext(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (CheckRun, StatusContext)


class UserListItems(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Repository,)


class VerifiableDomainOwner(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Enterprise, Organization)



########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

