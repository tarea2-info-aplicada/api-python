USE [Cattle]
GO

/****** Object:  StoredProcedure [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY]    Script Date: 17/11/2022 01:12:51 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

create   procedure [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY] 
AS
select [Year], (SELECT MONTH([Month] + '01 1900')) as Month ,[Weight],[Gender],[Price] from [dbo].[AveragePriceCattleSummary] where Price > 0;
Go:
GO


