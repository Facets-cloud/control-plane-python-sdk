# IoFabric8KubernetesApiModelPodSecurityContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_group** | **int** |  | [optional] 
**fs_group_change_policy** | **str** |  | [optional] 
**run_as_group** | **int** |  | [optional] 
**run_as_non_root** | **bool** |  | [optional] 
**run_as_user** | **int** |  | [optional] 
**se_linux_options** | [**IoFabric8KubernetesApiModelSELinuxOptions**](IoFabric8KubernetesApiModelSELinuxOptions.md) |  | [optional] 
**seccomp_profile** | [**IoFabric8KubernetesApiModelSeccompProfile**](IoFabric8KubernetesApiModelSeccompProfile.md) |  | [optional] 
**supplemental_groups** | **list[int]** |  | [optional] 
**sysctls** | [**list[IoFabric8KubernetesApiModelSysctl]**](IoFabric8KubernetesApiModelSysctl.md) |  | [optional] 
**windows_options** | [**IoFabric8KubernetesApiModelWindowsSecurityContextOptions**](IoFabric8KubernetesApiModelWindowsSecurityContextOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

