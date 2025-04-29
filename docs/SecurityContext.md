# SecurityContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_privilege_escalation** | **bool** |  | [optional] 
**capabilities** | [**Capabilities**](Capabilities.md) |  | [optional] 
**privileged** | **bool** |  | [optional] 
**proc_mount** | **str** |  | [optional] 
**read_only_root_filesystem** | **bool** |  | [optional] 
**run_as_group** | **int** |  | [optional] 
**run_as_non_root** | **bool** |  | [optional] 
**run_as_user** | **int** |  | [optional] 
**se_linux_options** | [**SELinuxOptions**](SELinuxOptions.md) |  | [optional] 
**seccomp_profile** | [**SeccompProfile**](SeccompProfile.md) |  | [optional] 
**windows_options** | [**WindowsSecurityContextOptions**](WindowsSecurityContextOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

