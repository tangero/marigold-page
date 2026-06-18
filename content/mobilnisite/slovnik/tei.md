---
slug: "tei"
url: "/mobilnisite/slovnik/tei/"
type: "slovnik"
title: "TEI – Terminal End-point Identifier"
date: 2025-01-01
abbr: "TEI"
fullName: "Terminal End-point Identifier"
category: "Identifier"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tei/"
summary: "Jedinečný identifikátor používaný ve specifikaci 3GPP TS 52.021 pro funkci adaptace terminálu (TAF). Rozlišuje jednotlivé koncové body uvnitř terminálu, což umožňuje správné směrování a správu dat mez"
---

TEI (identifikátor koncového bodu terminálu) je jedinečný identifikátor používaný uvnitř terminálu k rozlišení jednotlivých koncových bodů pro správné směrování dat mezi mobilním terminálem a sítí.

## Popis

Terminal End-point Identifier (TEI) je základní adresovací prvek definovaný ve specifikaci 3GPP TS 52.021, která detailně popisuje funkci adaptace terminálu ([TAF](/mobilnisite/slovnik/taf/)) pro sítě 3GPP GSM/UMTS. TEI funguje v kontextu TAF, která je zodpovědná za adaptaci datových proudů z koncového zařízení ([TE](/mobilnisite/slovnik/te/)) pro přenos přes mobilní síť, často zahrnující protokoly řady V.xx pro služby přepojování okruhů. Z architektonického hlediska je TEI přiřazen každému logickému koncovému bodu nebo datové relaci iniciované koncovým zařízením. Funguje jako lokální identifikátor na vrstvě datového spoje (konkrétně v rámci protokolů rodiny [LAP](/mobilnisite/slovnik/lap/) adaptovaných TAF), což síti umožňuje multiplexovat a demultiplexovat datové proudy patřící různým aplikacím nebo relacím pocházejícím ze stejného fyzického terminálu.

Během provozu, když je zřízeno datové volání, síť přiřadí TEI konkrétnímu koncovému bodu. Tento identifikátor je pak použit ve všech následujících datových rámcích vyměňovaných mezi mobilní stanicí a propojovací funkcí ([IWF](/mobilnisite/slovnik/iwf/)) sítě. TEI je klíčový pro ohraničení rámců a jejich správné doručení, zajišťuje, aby data určená pro jednu aplikaci (např. faxovou relaci) nebyla chybně doručena jiné (např. modemové relaci), která sdílí stejný fyzický rádiový prostředek. Jeho role je analogická identifikátorům datových spojů ([DLCI](/mobilnisite/slovnik/dlci/)) ve Frame Relay nebo identifikátorům virtuálních kanálů (VCI) v [ATM](/mobilnisite/slovnik/atm/), poskytuje mechanismus adresování vrstvy 2 pro virtuální okruhy.

Správa TEI zahrnuje procedury přiřazení, ověření a uvolnění koordinované mezi terminálem a sítí. Je klíčovou součástí spolehlivého přenosu nehlasových dat přes starší domény s přepojováním okruhů, podporující služby jako fax, data s přepojováním okruhů a raný přístup k mobilnímu internetu. I když jeho význam poklesl s dominancí paketově přepínaných IP sítí v 4G a 5G, pochopení TEI je nezbytné pro porozumění vývoje mobilních datových služeb a vzájemného propojení tradičních telekomunikačních protokolů a mobilních systémů.

## K čemu slouží

TEI byl vytvořen, aby vyřešil základní problém podpory více současných datových relací nebo logických kanálů z jednoho kusu koncového zařízení přes jediné fyzické připojení k síti GSM/UMTS. Před standardizovanou adaptací mobilních dat bylo připojování datových terminálů (jako laptopů s modemy) k mobilním sítím proprietární a neefektivní. Funkce adaptace terminálu ([TAF](/mobilnisite/slovnik/taf/)) a z ní vyplývající TEI poskytly standardizovaný způsob adaptace datových proudů z různých typů koncových zařízení (používajících rozhraní jako V.24/V.28) na protokoly používané přes rozhraní vzduchu.

Primární motivací bylo umožnit robustní služby dat s přepojováním okruhů, jako je fax a vytáčený internet, v éře 2G a 3G. Bez jedinečného identifikátoru koncového bodu, jako je TEI, by síť nebyla schopna rozlišit různé datové proudy multiplexované přes stejný rádiový kanál, což by vedlo ke zkreslení dat a neschopnosti současně podporovat více aplikací. TEI tak řešil omezení spočívající v existenci pouze jediného, nediferencovaného přenosového kanálu pro data, umožnil logické oddělení kanálů a správnou správu relací v rámci omezení technologie přepojování okruhů.

## Klíčové vlastnosti

- Jednoznačná identifikace logických koncových bodů uvnitř terminálu
- Umožňuje multiplexování více datových relací přes jediné fyzické připojení
- Funguje na vrstvě datového spoje (vrstva 2) zásobníku protokolů
- Nezbytný pro funkci adaptace terminálu (TAF) definovanou v TS 52.021
- Podporuje služby dat s přepojováním okruhů, jako je fax a modemová volání
- Usnadňuje správné směrování datových rámců mezi terminálem a propojovací funkcí sítě

## Definující specifikace

- **TS 52.021** (Rel-19) — GSM A-bis Interface Network Management

---

📖 **Anglický originál a plná specifikace:** [TEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tei/)
