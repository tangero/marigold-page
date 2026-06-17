---
slug: "mgcp"
url: "/mobilnisite/slovnik/mgcp/"
type: "slovnik"
title: "MGCP – Media Gateway Control Part"
date: 2025-01-01
abbr: "MGCP"
fullName: "Media Gateway Control Part"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mgcp/"
summary: "Media Gateway Control Part (MGCP) je protokol, standardizovaný IETF a referencovaný v 3GPP, používaný pro ovládání mediálních bran (Media Gateways) z externích prvků řízení hovorů, jako jsou Media Gat"
---

MGCP je protokol, standardizovaný IETF a referencovaný v 3GPP, pro ovládání mediálních bran (Media Gateways) z externích prvků řízení hovorů, jako jsou Media Gateway Controllers.

## Popis

Media Gateway Control Part (MGCP), definovaný v [IETF](/mobilnisite/slovnik/ietf/) RFC 3435 (nahrazeném RFC 3661), je textový protokol typu master-slave navržený pro ovládání mediálních bran ([MGW](/mobilnisite/slovnik/mgw/)) v dekomponované síťové architektuře. V tomto modelu je inteligence pro řízení hovorů umístěna v externí entitě – Media Gateway Controlleru ([MGC](/mobilnisite/slovnik/mgc/)), Call Agentovi nebo Softswitchi – zatímco MGW je 'hloupé' zařízení zodpovědné pouze za zpracování a přepínání médií. MGCP je mechanismus, kterým řadič příkazuje bráně k vytváření, modifikaci a ukončování mediálních spojení. Protokol je transakční, přičemž řadič posílá příkazy (jako CreateConnection, ModifyConnection, DeleteConnection) a brána odpovídá potvrzeními a oznámeními o událostech.

MGCP modeluje mediální bránu jako kolekci koncových bodů a spojení. Koncové body jsou zdroje nebo cíle mediálních dat, které mohou být fyzické (např. DS0 timeslot na lince T1) nebo virtuální (např. RTP proud pro paketový audio). Spojení jsou logická přidružení mezi koncovými body pro vytvoření mediální cesty. Řadič používá MGCP k tomu, aby nařídil bráně umístit koncové body do kontextů (které jsou jako větve hovoru nebo míchací body) a specifikovat, jak by měla média mezi nimi proudit. Protokol také umožňuje řadiči požádat bránu o detekci událostí (jako [DTMF](/mobilnisite/slovnik/dtmf/) číslice, faxové tóny nebo přechody zvednutí/odložení sluchátka) a o generování signálů (jako vyzváněcí tón, zpětný vyzváněcí tón nebo obsazovací tón). Veškerá hovorová logika, včetně analýzy číslic, směrování a spouštění služeb, je zpracována řadičem; brána pouze vykonává příkazy.

Zatímco MGCP byl vlivný v raných nasazeních Voice over IP (VoIP) a softswitchů, 3GPP nakonec vybralo H.248/[MEGACO](/mobilnisite/slovnik/megaco/) jako svůj standardizovaný protokol pro rozhraní Mc mezi MGC/[MGCF](/mobilnisite/slovnik/mgcf/) a MGW/[IMS-MGW](/mobilnisite/slovnik/ims-mgw/). H.248 je robustnější a flexibilnější nástupce, vyvinutý společně IETF a [ITU-T](/mobilnisite/slovnik/itu-t/). Architektura MGCP však přímo ovlivnila dekomponovaný model brány, který se stal ústředním pro návrh jádrové sítě 3GPP od Release 99 dále. Porozumění MGCP poskytuje historický kontext pro vývoj směrem k plně standardizovanému protokolu H.248 používanému v moderních sítích.

## K čemu slouží

MGCP byl vyvinut pro řešení potřeby standardizovaného rozhraní pro ovládání relativně jednoduchých, nízkonákladových mediálních bran z inteligentních serverů řízení hovorů. Před jeho vývojem byly rané VoIP brány často monolitické nebo používaly proprietární řídicí protokoly, což vedlo k závislosti na dodavateli a brzdilo inovace. MGCP vzešel z pracovní skupiny Megaco IETF (a dřívějších prací) za účelem podpory interoperability a urychlení přijetí paketové telefonie oddělením funkce řízení hovorů, která mohla být implementována v softwaru na standardních serverech, od funkce zpracování médií, která mohla být škálována nezávisle.

Jeho vznik byl motivován přechodem telekomunikačního průmyslu k paketově přepínaným sítím a snahou replikovat telefonní služby na IP infrastruktuře. MGCP vyřešil problém, jak ovládat distribuované mediální zdroje (brány na okraji sítě) z centralizovaného bodu inteligence, což umožnilo nové služby a efektivnější síťové návrhy. Ačkoli 3GPP později standardizovalo H.248 pro jeho větší škálovatelnost a sadu funkcí (podpora multimédií a více řídicích asociací), MGCP sehrál klíčovou historickou roli v ověření konceptu dekomponované brány a byl široce nasazován v před-IMS a raných architekturách NGN.

## Klíčové vlastnosti

- Textový, transakční protokol typu master-slave pro ovládání mediální brány
- Modeluje brány pomocí koncových bodů (fyzických/virtuálních) a spojení
- Příkazy zahrnují CreateConnection, ModifyConnection, DeleteConnection a NotificationRequest
- Podporuje detekci událostí (DTMF, hook-flash) a generování signálů (tóny, hlášení)
- Umožňuje centralizovanou logiku řízení hovorů oddělenou od distribuovaného zpracování médií
- Používá jednoduchý model příkaz-odpověď přes UDP nebo TCP

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MGCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgcp/)
