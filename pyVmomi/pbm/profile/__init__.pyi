from typing import List
from enum import Enum
from pyVmomi import pbm, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, long
from . import provider


class ProfileManager(ManagedObject):
    def FetchResourceType(self) -> List[ResourceType]: ...
    def FetchVendorInfo(self, resourceType: ResourceType) -> List[pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo]: ...
    def FetchCapabilityMetadata(self, resourceType: ResourceType, vendorUuid: str) -> List[pbm.capability.provider.CapabilityObjectMetadataPerCategory]: ...
    def FetchCapabilitySchema(self, vendorUuid: str, lineOfService: List[str]) -> List[pbm.capability.provider.CapabilityObjectSchema]: ...
    def Create(self, createSpec: CapabilityBasedProfileCreateSpec) -> ProfileId: ...
    def Update(self, profileId: ProfileId, updateSpec: CapabilityBasedProfileUpdateSpec) -> NoneType: ...
    def Delete(self, profileId: List[ProfileId]) -> List[ProfileOperationOutcome]: ...
    def QueryProfile(self, resourceType: ResourceType, profileCategory: str) -> List[ProfileId]: ...
    def RetrieveContent(self, profileIds: List[ProfileId]) -> List[Profile]: ...
    def QueryAssociatedProfiles(self, entities: List[pbm.ServerObjectRef]) -> List[QueryProfileResult]: ...
    def QueryAssociatedProfile(self, entity: pbm.ServerObjectRef) -> List[ProfileId]: ...
    def QueryAssociatedEntity(self, profile: ProfileId, entityType: str) -> List[pbm.ServerObjectRef]: ...
    def QueryDefaultRequirementProfile(self, hub: pbm.placement.PlacementHub) -> ProfileId: ...
    def ResetDefaultRequirementProfile(self, profile: ProfileId) -> NoneType: ...
    def AssignDefaultRequirementProfile(self, profile: ProfileId, datastores: List[pbm.placement.PlacementHub]) -> NoneType: ...
    def FindApplicableDefaultProfile(self, datastores: List[pbm.placement.PlacementHub]) -> List[Profile]: ...
    def QueryDefaultRequirementProfiles(self, datastores: List[pbm.placement.PlacementHub]) -> List[DefaultProfileInfo]: ...
    def ResetVSanDefaultProfile(self) -> NoneType: ...
    def QuerySpaceStatsForStorageContainer(self, datastore: pbm.ServerObjectRef, capabilityProfileId: List[ProfileId]) -> List[provider.DatastoreSpaceStatistics]: ...
    def QueryAssociatedEntities(self, profiles: List[ProfileId]) -> List[QueryProfileResult]: ...


class CapabilityBasedProfile(Profile):
    @property
    def profileCategory(self) -> str: ...
    @property
    def resourceType(self) -> ResourceType: ...
    @property
    def constraints(self) -> CapabilityConstraints: ...
    @property
    def generationId(self) -> long: ...
    @property
    def isDefault(self) -> bool: ...
    @property
    def systemCreatedProfileType(self) -> str: ...
    @property
    def lineOfService(self) -> str: ...


    class ProfileCategoryEnum(Enum):
        REQUIREMENT = "requirement"
        RESOURCE = "resource"
        DATA_SERVICE_POLICY = "data_service_policy"


    class SystemCreatedProfileType(Enum):
        VsanDefaultProfile = "vsandefaultprofile"
        VVolDefaultProfile = "vvoldefaultprofile"
        PmemDefaultProfile = "pmemdefaultprofile"
        VmcManagementProfile = "vmcmanagementprofile"
        VsanMaxDefaultProfile = "vsanmaxdefaultprofile"


class CapabilityBasedProfileCreateSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def category(self) -> str: ...
    @property
    def resourceType(self) -> ResourceType: ...
    @property
    def constraints(self) -> CapabilityConstraints: ...


class CapabilityBasedProfileUpdateSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def constraints(self) -> CapabilityConstraints: ...


class CapabilityConstraints(vmodl.DynamicData): ...


class DataServiceToPoliciesMap(vmodl.DynamicData):
    @property
    def dataServicePolicy(self) -> ProfileId: ...
    @property
    def parentStoragePolicies(self) -> List[ProfileId]: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class DefaultCapabilityBasedProfile(CapabilityBasedProfile):
    @property
    def vvolType(self) -> List[str]: ...
    @property
    def containerId(self) -> str: ...


class DefaultProfileInfo(vmodl.DynamicData):
    @property
    def datastores(self) -> List[pbm.placement.PlacementHub]: ...
    @property
    def defaultProfile(self) -> Profile: ...


class Profile(vmodl.DynamicData):
    @property
    def profileId(self) -> ProfileId: ...
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def creationTime(self) -> datetime: ...
    @property
    def createdBy(self) -> str: ...
    @property
    def lastUpdatedTime(self) -> datetime: ...
    @property
    def lastUpdatedBy(self) -> str: ...


class ProfileId(vmodl.DynamicData):
    @property
    def uniqueId(self) -> str: ...


class ProfileOperationOutcome(vmodl.DynamicData):
    @property
    def profileId(self) -> ProfileId: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class ProfileType(vmodl.DynamicData):
    @property
    def uniqueId(self) -> str: ...


class QueryProfileResult(vmodl.DynamicData):
    @property
    def object(self) -> pbm.ServerObjectRef: ...
    @property
    def profileId(self) -> List[ProfileId]: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class ResourceType(vmodl.DynamicData):
    @property
    def resourceType(self) -> str: ...


class SubProfileCapabilityConstraints(CapabilityConstraints):
    @property
    def subProfiles(self) -> List[SubProfileCapabilityConstraints.SubProfile]: ...


    class SubProfile(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @property
        def capability(self) -> List[pbm.capability.CapabilityInstance]: ...
        @property
        def forceProvision(self) -> bool: ...


class AssociateAndApplyPolicyStatus():


    class PolicyStatus(Enum):
        success = "success"
        failed = "failed"
        invalid = "invalid"


class EntityAssociations():


    class Operation(Enum):
        CREATE = "create"
        REGISTER = "register"
        RECONFIGURE = "reconfigure"
        MIGRATE = "migrate"
        CLONE = "clone"


class IofilterInfo():


    class FilterType(Enum):
        INSPECTION = "inspection"
        COMPRESSION = "compression"
        ENCRYPTION = "encryption"
        REPLICATION = "replication"
        CACHE = "cache"
        DATAPROVIDER = "dataprovider"
        DATASTOREIOCONTROL = "datastoreiocontrol"


class PolicyAssociation():


    class VolumeAllocationType(Enum):
        FullyInitialized = "fullyinitialized"
        ReserveSpace = "reservespace"
        ConserveSpaceWhenPossible = "conservespacewhenpossible"


class VmAssociations(): ...