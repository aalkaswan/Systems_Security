
void UndefinedFunction_40201190(uint *param_1,byte *param_2,uint param_3)

{
  int *piVar1;
  undefined *puVar2;
  bool bVar3;
  int iVar4;
  uint *puVar5;
  
  piVar1 = DAT_402010b4;
  PRINT_FUN(DAT_402010b4,(uint *)PTR_s_Message_arrived___40201164);
  PRINT_FUN(piVar1,param_1);
  PRINT_FUN(piVar1,(uint *)PTR_DAT_40201168);
  puVar2 = PTR_DAT_4020116c;
  iVar4 = (*DAT_40201114)(param_2,PTR_DAT_4020116c,param_3);
  puVar5 = (uint *)PTR_DAT_40201170;
  if (iVar4 == 0) {
    iVar4 = 1;
    puVar5 = (uint *)puVar2;
LAB_402011ea:
    (*(code *)PTR_FUN_4020118c)(2,iVar4);
  }
  else {
    iVar4 = (*DAT_40201114)(param_2,PTR_DAT_40201170,param_3);
    if (iVar4 == 0) goto LAB_402011ea;
    if (param_3 < 9) {
      puVar5 = (uint *)PTR_s_Unknown_40201188;
      if (param_3 == 3) {
        if (((uint)(param_2[2] ^ *param_2) ^ (uint)param_2[1] << 1) == 0x68) {
          iVar4 = 0x14;
          do {
            (*(code *)PTR_FUN_4020118c)(2,0);
            WAIT_FUN(0x28);
            (*(code *)PTR_FUN_4020118c)(2,1);
            iVar4 = iVar4 + -1;
            WAIT_FUN(0x28);
          } while (iVar4 != 0);
          goto LAB_4020129d;
        }
      }
      else {
        if (6 < param_3) goto LAB_40201271;
      }
    }
    else {
      iVar4 = (*DAT_40201114)(param_2,PTR_s_restart_40201174);
      if (iVar4 == 0) {
        bVar3 = FUN_40201118((uint *)(param_2 + 8),param_3 - 8);
        if (bVar3 != false) {
          PRINT_FUN2(piVar1,(uint *)PTR_s_Restart_40201178);
          FUN_4020bd4c();
        }
        goto LAB_4020129d;
      }
LAB_40201271:
      iVar4 = (*DAT_40201114)(param_2,PTR_s_ADMIN_40201180,6);
      puVar5 = (uint *)PTR_s_Unknown_40201188;
      if (iVar4 == 0) {
        bVar3 = FUN_40201118((uint *)(param_2 + 6),param_3 - 6);
        if (bVar3 != false) {
          *DAT_40201184 = 1;
        }
        goto LAB_4020129d;
      }
    }
  }
  PRINT_FUN(piVar1,puVar5);
LAB_4020129d:
  FUN_4020c480(piVar1);
  return;
}

