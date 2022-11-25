USE [Cattle]
GO

/****** Object:  StoredProcedure [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY]    Script Date: 21/11/2022 03:22:02 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE or alter   procedure [dbo].[SP_AVERAGE_PRICE_CATTLE_SUMMARY] 
AS
select [Year], (SELECT MONTH([Month] + '01 1900')) as Month ,[Gender], CAST([Price] as int) as Price  from [dbo].[AveragePriceCattleSummary] where Price > 0;
Go:
GO

