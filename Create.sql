DROP TABLE IF EXISTS [dbo].[Fact_RealEstate];
DROP TABLE IF EXISTS [dbo].[Dim_Date];
DROP TABLE IF EXISTS [dbo].[Dim_Town];
DROP TABLE IF EXISTS [dbo].[Dim_PropertyType];
DROP TABLE IF EXISTS [dbo].[Dim_ResidentialType];
DROP TABLE IF EXISTS [dbo].[Dim_ResidentialType];
DROP TABLE IF EXISTS [dbo].[Dim_NonUseCode];

CREATE TABLE [dbo].[Fact_RealEstate](
	[Serial_Number] [bigint] NULL,
	[List_Year] [bigint] NULL,
	[Address] [varchar](max) NULL,
	[Assessed_Value] [float] NULL,
	[Sale_Amount] [float] NULL,
	[Sales_Ratio] [varchar](max) NULL,
	[Assessor_Remarks] [varchar](max) NULL,
	[OPM_remarks] [varchar](max) NULL,
	[Location] [varchar](max) NULL);

CREATE TABLE [dbo].[Dim_Date](
	[Date_Recorded] [varchar](max) NULL);

CREATE TABLE [dbo].[Dim_Town](
	[Town] [varchar](max) NULL);

CREATE TABLE [dbo].[Dim_PropertyType](
	[Property_Type] [varchar](max) NULL);

CREATE TABLE [dbo].[Dim_ResidentialType](
	[Residential_Type] [varchar](max) NULL);

CREATE TABLE [dbo].[Dim_NonUseCode](
	[Non_Use_Code] [varchar](max) NULL);