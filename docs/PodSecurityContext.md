# PodSecurityContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_group** | **int** |  | [optional] 
**fs_group_change_policy** | **str** |  | [optional] 
**run_as_group** | **int** |  | [optional] 
**run_as_non_root** | **bool** |  | [optional] 
**run_as_user** | **int** |  | [optional] 
**se_linux_options** | [**SELinuxOptions**](SELinuxOptions.md) |  | [optional] 
**seccomp_profile** | [**SeccompProfile**](SeccompProfile.md) |  | [optional] 
**supplemental_groups** | **list[int]** |  | [optional] 
**sysctls** | [**list[Sysctl]**](Sysctl.md) |  | [optional] 
**windows_options** | [**WindowsSecurityContextOptions**](WindowsSecurityContextOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

