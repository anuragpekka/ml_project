import os
import sys
from unittest.util import strclass

class HousingException(Exception): #Inheriting Exception
    #err_message:Exception means that err_message will be a instance of Exception
    #sys has  info of the error like whic line is causing error
    def __init__(self, err_message:Exception, err_detail:sys):
        super().__init__(err_message) #passing args to Parent class, Exception
        
        #self.error_message = err_message
        self.error_message = HousingException.get_detailed_error_message(err_message=err_message,
                                                                         err_detail=err_detail
                                                                        )
        
    @staticmethod
    #Won't have self arg
    def get_detailed_error_message(err_message:Exception, err_detail:sys)->str:
        _, _, exec_tb = err_detail.exc_info() #exc_info - returns (type,value,traceback)
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in File: [{file_name}] at Line number: [{line_number}] Error message: [{err_message}]"
        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self)->str:
        return HousingException.__name__.str()



