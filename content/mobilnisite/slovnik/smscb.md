---
slug: "smscb"
url: "/mobilnisite/slovnik/smscb/"
type: "slovnik"
title: "SMSCB – Short Message Service Cell Broadcast"
date: 2025-01-01
abbr: "SMSCB"
fullName: "Short Message Service Cell Broadcast"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/smscb/"
summary: "SMSCB je služba typu bod–více bodů, která vysílá krátké zprávy všem mobilním zařízením v určité geografické oblasti, jako je buňka nebo skupina buněk. Používá se pro systémy veřejného varování, lokali"
---

SMSCB je služba typu bod–více bodů, která vysílá krátké zprávy všem mobilním zařízením v určité geografické oblasti pro veřejná varování, lokalizační informace a nouzové výstrahy.

## Popis

Short Message Service Cell Broadcast (SMSCB) je služba vysílání zpráv definovaná ve standardech GSM a UMTS. Umožňuje operátorovi sítě nebo autorizované entitě odeslat jedinou zprávu, která je současně doručena všem kompatibilním mobilním stanicím nacházejícím se v definované sadě buněk, známé jako vysílací oblast. Služba funguje na vyhrazeném logickém kanálu, Cell Broadcast Channel ([CBCH](/mobilnisite/slovnik/cbch/)), který je namapován na fyzický kanál v buňce. Zprávy jsou opakovaně vysílány po stanovenou dobu, aby je mohla přijmout zařízení, která do oblasti vstoupila nebo byla dočasně neaktivní. Obsah a plánování řídí Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), což je síťová entita zodpovědná za správu a distribuci vysílacích zpráv příslušným řadičům základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) nebo řadičům rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)).

Z architektonického hlediska jsou klíčovými komponentami Cell Broadcast Centre (CBC), základnový stanicový systém ([BSS](/mobilnisite/slovnik/bss/)) nebo rádiová přístupová síť (RAN) a mobilní stanice. CBC, specifikované v 3GPP TS 23.041, je vstupním bodem pro vysílací zprávy. Autentizuje zdroje zpráv, formátuje zprávy podle protokolu Cell Broadcast a určuje geografický rozsah (seznam buněk) a parametry opakování. CBC se připojuje k BSC v GSM nebo k RNC v UMTS prostřednictvím rozhraní [CBC-BSC](/mobilnisite/slovnik/cbc-bsc/) nebo CBC-RNC (specifikováno v TS 48.049) za použití protokolů Base Station System Application Part ([BSSAP](/mobilnisite/slovnik/bssap/)) nebo Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)). BSC/RNC poté naplánuje vysílání na rádiovém rozhraní pomocí protokolu Cell Broadcast přes CBCH.

Na rádiovém rozhraní jsou zprávy SMSCB přenášeny jako série stránek na CBCH. Každá zpráva má identifikátor zprávy a sériové číslo, což mobilnímu zařízení umožňuje identifikovat nová vysílání a ignorovat duplikáty. Software Cell Broadcast v mobilním zařízení tyto stránky zpracuje, znovu sestaví zprávu a zobrazí ji uživateli na základě uživatelských nastavení (např. které identifikátory zpráv zobrazit). Jedna vysílací zpráva může mít až 93 alfanumerických znaků (ve výchozím kódování) a není potvrzována; neexistuje zpětná vazba od mobilních zařízení k síti ohledně přijetí. To ji činí vysoce škálovatelnou pro hromadnou distribuci, ale nevhodnou pro garantované individuální doručení.

Služba podporuje seskupování zpráv a stanovení priority. Zprávy jsou kategorizovány pomocí identifikátoru zprávy, který může označovat typ zprávy (např. veřejné varování, komerční informace). Geografický rozsah je definován vysílací oblastí, která může být jedna buňka, oblast umístění nebo vlastní sada buněk. CBC spravuje mapování identifikátorů zpráv na vysílací oblasti. SMSCB je z podstaty efektivní pro síťové zdroje, protože jeden přenos v buňce dosáhne všech zařízení naslouchajících danému kanálu, na rozdíl od SMS typu bod–bod, která vyžaduje individuální signalizační transakce pro každého příjemce. Tato efektivita je klíčová pro systémy nouzových výstrah, kde je vyžadováno včasné a rozsáhlé rozšíření.

## K čemu slouží

SMSCB byl vyvinut k poskytnutí možnosti vysílání typu jeden–více v rámci mobilní sítě, aby uspokojil potřebu šíření informací všem uživatelům v určité geografické oblasti bez signalizační režie individuálních zpráv. Jeho primárním účelem jsou systémy veřejných informací a varování, jako jsou výstrahy před zemětřesením nebo tsunami, varování před nepříznivým počasím a AMBER výstrahy pro únosy dětí. Řeší problém, jak rychle a spolehlivě informovat velkou populaci v ohrožené oblasti, což se po velkých katastrofách stalo regulačním požadavkem v mnoha zemích.

Historicky, před rozšířením chytrých telefonů a lokalizačních služeb, byl SMSCB jedním z mála způsobů, jak implementovat cílená hromadná oznámení pomocí mobilní infrastruktury. Využíval existující mechanismus rádiového vysílání (CBCH), který byl původně definován v raných standardech GSM, ale významnou standardizaci a podporu získal od 3GPP Release 8 dále, zejména pro požadavky Public Warning System (PWS). Omezení SMS typu bod–bod pro nouzové výstrahy jsou zřejmá: během krize mohou být signalizační sítě přetížené a doručení milionů individuálních zpráv je pomalé a může selhat. SMSCB se tomu vyhýbá použitím vysílacího kanálu, který je robustnější při vysokém zatížení.

Vytvoření a vylepšení SMSCB bylo motivováno také komerčními aplikacemi, jako je vysílání dopravních informací, reklamy nebo titulků zpráv účastníkům na konkrétním místě, jako je letiště nebo nákupní centrum. Jeho nejkritičtější role se však vyvinula v podporu vládou nařízených varovných systémů. 3GPP integrovalo SMSCB s požadavky Earthquake and Tsunami Warning System (ETWS) a Commercial Mobile Alert System (CMAS), definující specifické identifikátory zpráv a postupy. To zajistilo standardizovanou, interoperabilní metodu pro záchranná varování napříč různými sítěmi a výrobci zařízení, čímž se stal SMSCB klíčovou součástí moderní infrastruktury veřejné bezpečnosti.

## Klíčové vlastnosti

- Vysílá zprávy všem nečinným i aktivním mobilním zařízením v definované sadě buněk bez individuálního adresování
- Používá vyhrazený Cell Broadcast Channel (CBCH) na rádiovém rozhraní pro efektivní využití spektra
- Spravován Cell Broadcast Centre (CBC), které řídí obsah zpráv, geografický rozsah a plánování
- Podporuje identifikátory zpráv a sériová čísla pro kategorizaci zpráv a detekci duplikátů mobilními zařízeními
- Integrován se systémy veřejného varování (PWS), jako jsou ETWS a CMAS, pro nouzové výstrahy
- Škálovatelná architektura s minimální signalizační režií sítě ve srovnání s SMS typu bod–bod

## Související pojmy

- [CBC – Cipher Block Chaining (Mode)](/mobilnisite/slovnik/cbc/)
- [CBCH – Cell Broadcast Channel](/mobilnisite/slovnik/cbch/)

## Definující specifikace

- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification
- **TS 48.049** (Rel-19) — Cell Broadcast Service Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SMSCB na 3GPP Explorer](https://3gpp-explorer.com/glossary/smscb/)
