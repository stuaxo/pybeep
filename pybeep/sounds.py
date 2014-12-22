import base64

"""
Various sound clips
"""
beep_bytes = base64.b64decode(
b'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\
kVr4GVFtQAZ5M3h2IuFzlz/nQCACAMC29HWM1z+WMu9UAkAkCHvB6Pen3v3t96AIP/7EGRDA/BzAMRAQhgKDQAY9QBjAUHIAxaBCCAoKgBkABCMB80hlgyGOCuactsEVG4zxUfDSsOiXGtqEgAAABnvZOg8oSGl9pPIQAgCAC5GPDeuj4ZdHVwRjCAyqxzWv1jP23j1\
AUW6//sSZEqDMGYAxChDEA4M4BkVBCMBwagDEwCEYCgvgCQUEIyfnE59jtunAAzkcAoUBsJhBn6vhzdunWM8roUAQAAKCTBGHBDgB6va4oaCRD6gQRQGd4IzJIVgwybvVsWplSIFJMJMSIoB//sQZFODMHQBRCCjEAoNwBkkBEMBQXgDEKEEYDgxgqQUEIgNFSPIkxR\
4+4NVAAFAAIarOUZHQai8dyheDh8AIABt5gI4kPtkzk6Qh5JEgJktcIyEPjiGSmkB1qx1G2B7ngos0ig0a4X/+xJkWwMweQXDwEEQmg3gGRgAIwFBkAMPAwhAKDgAJGAQjJ0HJhmytE5cVHkSGCJAVIUTKMqsGUWKAJISIgxQwWVZEVifHyZKcgrUZDOAAfXDl9ZRhA\
UF2GgJ3ng40g6iwZO0dIABdZD/+xBkYYMwcgDGICEQChXBuMQMYydBmAMhwIhgIEWCJFAQjAUTRgbsmcDKhVDbRSriAECAwEdPVnJGcwYEhaQmHFDw5yQwySQAAGLRDjBIlfdoKQI/EPJCAAZy0wIDKggjO88R9JGKUv/7EmRiB7CIDEOhAhk4GqHolRkpJ4F4Jwqji\
ESwZAdiFGSknJkLZN3vE4nRzAUCIJeLerQy+33+WdgYEKDAy8Ux15ZBQsOh803X5ItbrQRIAAAaj7AorccMWRAAAIQAY6g0rp62cZMHEf/7EGRcAzCLCMSgYxiqGWHouBjGJwG8GQqiiEJ4ZYdi4CMYnDIQv8CeiNDHevMfsoZRAvYU9wPjHbgaAdyj3EDbqyZRMKoU\
yaZW2cXCqhbaKCQHiZiP6i1p5v7tmASQAVgYynDn2I6I//sSZFUDcHwKRCihGS4aQdiFGSknAZADFQCEQChShyKANJiftYXVCbQegRkCM4dXvREx67/iqCQBRKglNGdB4SsxJN6jrVECagIfkU51IFwoMo2AwVIMnIAAAAtQK0zQwPElOwHx5x4E//sQZFIDsGkDw0B\
iEAgUgci4DMYnAdwzBAWYpOhPhuKUYxidwBBJXm19mHXtz/lmEcAJiyDxWBAL5XRVaGsg5DIAOCAADHTb72W+LhX/CAAAYAJMBM0FKkkqIJyeNQ1MQU1FMy45OS7/+xJkUYMwbgDGoCEQChJhyPgMQycBnDcRAQhE4EUG4+AxjJ01VVVVVVVVVVVVVVVVVVVVVVVVVV\
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVX/+xBkVIMwdgpCASUpKhAgCSQEIydBpAMPAwRAKEMGo+AxjJ1VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\
VVVVf/7EmRYD/BuAL/AQRAKD+BYeARhAUAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVQ=='
)



vibrate_bytes = base64.b64decode(
b'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\
PaRGoWSY5u5vAaZb4iUAzyc5yvvxf/7FGSKD/B7DVOCQRk6C8BKMGBiAQG0OU4JhGTgNARogaCIVDhwYOwWIIYHBCOBZo5ukMKx4YDKMQubrGt7MR45KqgMWg13FxRjqBcBeEuIHaDGuRUu2/7yKjvpZoDhFP/7FGSND/BzDlKCIRk4DWBaEGTBAUG0CUQMGGAoNAEo\
AZGMBRbAaI9Vi0V3C8CBciHsoLLXGPe62hw7zmhlZaCVFs7Mt/dgYLIIWIowZOIU2Mu1NIo/GLeMgJaYDSzzLP/7FGSPj/B7C9CB4Rk6DOCp8GDCAwHcJz4MhESoMQInQYGMBZiQAgUAADGUU5DN7vN0RdmZiiQGQEEHhYkF83QG8zihqDOyIdEdlRIksOshUIeE9XD\
aZn5URoOIVFsdBv/7FGSRj/B5CU8DARiqDSBpwGDCAUIULTgMDGToNYHmwYEMBLv34VkxQDixR6PuJFAEe5B92KADJlCAaUHuiV65cyYdheg1NQiGSDC3EqgNFaAAccRHnWnW2PRWHwSCDP/7FGSSD/BqBk6DARiaDQC5sDxiE0G4EzgMpGBoLwFmwYSEBTU2QEi1WA\
7wl2AEUmVDDjAKGrFsoXMqCAEjSQUmaSN23eKpR0A5UYCDIILxUuLq8ugyCMKMKJYsa0k/Uv/7FGSWD/B0BEsDKDAKC4CpkGAjA0HAGzAMFGJgNIIlwPEIBegMg2BlhngRfNbl+XRwynGQQAkhC2OKstYk6SG7wHC0NgNxmRTCUMAEJBAP0wUECHLd6SAiN5tWJu+El\
v/7FGSZD/ByBUqDBhAaDMCZYDzDA0GsEywMJGBoMgIlAMEMBWfLlQBAAGtPaaIj/5TsAQABZVyquG7+1aVMQU1FTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGScjzB2BsoDAhiaDCAZiCxBAUHIFyQMDEJgKoGkgPMMBVVVVVVVVVVVVVVVVVVVVVVV\
VVVVVVVVVVVVVVVVTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGSgj/BsBEcB6RgKDOC44CRjE0GoFxoHjGJgMYEjQMGIBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGSkjzBeBMU\
BgxgYDSAZCCQCAQGwExIEmGBoNABkEBEMBFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGSog/BqA8GBJjAKDGCIMCRDAUGMBRSBBEAgNgKgALEIDVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\
VVTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FESsgzBkAECgARgIDQGHwAgjJ0FEFMcAhGBoMAAfIBCIBVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGSyj/BWASqoYRgKCsAlVQwjA\
UAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuOTkuNVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGTFj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVTEFNRTMuOTku\
NVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA\
0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\
VVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVV\
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\
Vf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7FGThj/AAAGkAAAAIAAANIAAAAQAAAaQAAAAgAAA0gAAABFVVVVVVVVVVVVVVVVVVVVV\
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVQ=='
)
