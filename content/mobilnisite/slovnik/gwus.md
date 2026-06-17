---
slug: "gwus"
url: "/mobilnisite/slovnik/gwus/"
type: "slovnik"
title: "GWUS – Group Wake Up Signal"
date: 2025-01-01
abbr: "GWUS"
fullName: "Group Wake Up Signal"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gwus/"
summary: "Signál na fyzické vrstvě v NR navržený k efektivnímu probuzení skupiny uživatelských zařízení (UE) z klidového nebo neaktivního stavu. Snižuje spotřebu energie zařízení tím, že umožňuje UE vynechat mo"
---

GWUS je signál na fyzické vrstvě v NR navržený k efektivnímu probuzení skupiny UE z klidového (idle) nebo neaktivního (inactive) stavu, který snižuje spotřebu energie tím, že jim umožňuje vynechat monitorování přenosů na PDCCH, pokud nejsou tímto signálem vyzvány.

## Popis

Group Wake Up Signal (GWUS) je funkce zavedená v 5G New Radio (NR) pro vylepšení mechanismů úspory energie u připojených zařízení. Jedná se o signál na fyzické vrstvě s nízkou složitostí, který vysílá gNodeB (gNB), aby naznačil, zda se má konkrétní skupina UE, která je nakonfigurována k jeho monitorování, probudit a dekódovat následný Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). GWUS je přenášen na vyhrazeném zdroji, typicky před možnou příležitostí pro PDCCH, a je navržen tak, aby byl extrémně jednoduchý na detekci, což vyžaduje minimální zpracování přijímacím obvodem UE.

Z architektonického hlediska GWUS funguje v rámci mechanismu Discontinuous Reception ([DRX](/mobilnisite/slovnik/drx/)). UE ve stavech [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE se periodicky probouzejí, aby monitorovaly stránkování (paging) nebo jiné indikace. S GWUS je tento proces rozdělen do dvou kroků. Nejprve UE na krátkou dobu zapne svůj přijímač, aby zjistila přítomnost či nepřítomnost pro ni nakonfigurovaného GWUS. GWUS nese jednoduchou indikaci, často jen sekvenci nebo příznak, která signalizuje 'probudit se' nebo 'neprobouzet se' pro přidruženou skupinu. Pokud GWUS indikuje 'probudit se', UE následně plně zapne svůj hlavní přijímač a dekóduje PDCCH v nadcházející monitorovací příležitosti. Pokud GWUS indikuje 'neprobouzet se', UE se může okamžitě vrátit do stavu hlubokého spánku, čímž zcela vynechá energeticky mnohem náročnější proces dekódování PDCCH.

Klíčové komponenty zahrnují scheduler v gNB, který určuje, kdy vyslat GWUS pro konkrétní skupinu UE, a konfiguraci úspory energie v UE, která obsahuje parametry jako periodicita monitorování GWUS, časově-frekvenční zdroje a skupinové ID. Samotný signál je definován ve specifikacích fyzické vrstvy (např. jako specifická sekvence v Synchronization Signal Block (SSB) nebo vyhrazený referenční signál). Jeho role je klíčová pro use case Massive Machine-Type Communication (mMTC) a Enhanced Mobile Broadband (eMBB), kde je prvořadé prodloužení výdrže baterie, protože drasticky snižuje dobu, po kterou jsou vysokovýkonné základní pásmo (baseband) a RF komponenty UE aktivní.

## K čemu slouží

GWUS byl vytvořen k řešení základní výzvy výdrže baterie u neustále připojených 5G zařízení, zejména pro senzory Internetu věcí (IoT) a chytré telefony. Tradiční cykly [DRX](/mobilnisite/slovnik/drx/) stále vyžadovaly, aby UE plně dekódovalo [PDCCH](/mobilnisite/slovnik/pdcch/) během každé 'on duration' (doby zapnutí), aby zkontrolovalo naplánované příkazy, což spotřebovává značnou energii, i když pro UE nejsou naplánována žádná data. Toto 'slepé dekódování' bylo identifikováno jako hlavní zdroj zbytečného odběru energie, zejména pro zařízení s nízkou mírou aktivity.

Problém, který GWUS řeší, je neefektivita povinného monitorování PDCCH. Zavedením signálu předindikace s velmi nízkou spotřebou umožňuje síti včas sdělit skupině UE, zda potřebují vynaložit energii na plné zpracování PDCCH. Toto bylo motivováno cíli návrhu 5G pro masivní IoT, která vyžadují, aby zařízení měla výdrž baterie 10 let a více. GWUS poskytuje nástroj pro úsporu energie s jemnějším rozlišením než tradiční dlouhé cykly DRX, což umožňuje rychlejší reakční doby, když je to potřeba, a zároveň maximalizuje dobu spánku. Představuje vývoj od konceptu Wake-Up Signal (WUS) studovaného v LTE, který je nyní standardizován a optimalizován pro flexibilnější rámec NR, aby podporoval různé typy zařízení a vzorce provozu.

## Klíčové vlastnosti

- Fyzický signál s nízkou složitostí pro předindikaci
- Skupinová adresace pro současné probuzení více UE
- Snižuje spotřebu energie UE tím, že se vyhne zbytečnému dekódování PDCCH
- Konfigurovatelné monitorovací příležitosti synchronizované s cykly DRX
- Podpora stavů RRC_IDLE i RRC_INACTIVE
- Zlepšuje výdrž baterie pro IoT a mobilní zařízení

## Související pojmy

- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [GWUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gwus/)
