###############################################################################
#
# 
#
###############################################################################
THIS_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
x86_64_accton_asxvolt16b_INCLUDES := -I $(THIS_DIR)inc
x86_64_accton_asxvolt16b_INTERNAL_INCLUDES := -I $(THIS_DIR)src
x86_64_accton_asxvolt16b_DEPENDMODULE_ENTRIES := init:x86_64_accton_asxvolt16b ucli:x86_64_accton_asxvolt16b

