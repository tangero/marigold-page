---
slug: "srb2"
url: "/mobilnisite/slovnik/srb2/"
type: "slovnik"
title: "SRB2 – Signalling Radio Bearer 2"
date: 2025-01-01
abbr: "SRB2"
fullName: "Signalling Radio Bearer 2"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srb2/"
summary: "Specifický signalizační rádiový bearer používaný v UMTS a LTE pro přenos NAS zpráv po aktivaci zabezpečení. Je zřízen po navázání RRC spojení a zajišťuje signalizaci ne-přístupové vrstvy (NAS), jako j"
---

SRB2 je signalizační rádiový bearer používaný v UMTS a LTE pro přenos zpráv ne-přístupové vrstvy (NAS), například pro správu relací, po aktivaci zabezpečení a navázání RRC spojení.

## Popis

Signalling Radio Bearer 2 (SRB2) je specifický typ signalizačního rádiového beareru definovaný ve standardech 3GPP, používaný primárně v sítích UMTS a LTE. Je určen pro přenos zpráv ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)) mezi UE a jádrem sítě poté, co bylo navázáno počáteční spojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a aktivováno zabezpečení. Na rozdíl od SRB1, který přenáší RRC zprávy a může zpočátku přenášet i NAS zprávy, je SRB2 explicitně konfigurován pro NAS signalizaci, jakmile je spojení stabilnější a zabezpečené. SRB2 funguje přes rozhraní vzduchového rozhraní a je mapován na downlinkové a uplinkové transportní kanály, přičemž [RLC](/mobilnisite/slovnik/rlc/) je typicky konfigurováno v potvrzovaném režimu pro zajištění spolehlivého doručení.

Z architektonického hlediska je SRB2 zřizován během procedury navazování RRC spojení. Poté, co UE odešle na SRB1 zprávu RRCConnectionSetupComplete, která může obsahovat počáteční NAS zprávy, může síť nakonfigurovat SRB2 pomocí RRC rekonfiguračních zpráv. SRB2 se používá pro NAS zprávy související se správou relací, jako je Activate Default EPS Bearer Context Request, a další signalizaci jádra sítě. Funguje ve spolupráci se SRB1, kde SRB1 nadále přenáší RRC zprávy a případně některé NAS zprávy, zatímco SRB2 odlehčuje NAS-specifický provoz na samostatný bearer. Toto oddělení umožňuje efektivnější zpracování a prioritizaci signalizace.

Provoz SRB2 zahrnuje vrstvu RRC v UE a [eNB](/mobilnisite/slovnik/enb/) (nebo NodeB), která zřizuje bearer s konkrétními konfiguračními parametry, včetně identifikace logického kanálu a nastavení RLC. NAS zprávy z NAS vrstvy UE jsou zapouzdřeny do RRC kontejnerů a přenášeny přes SRB2. Na straně sítě eNB tyto kontejnery předává jádru sítě ([MME](/mobilnisite/slovnik/mme/) v LTE). SRB2 je zřízen až po aktivaci zabezpečení (ochrana integrity a šifrování), čímž je zajištěna ochrana citlivých NAS informací. Jeho role je klíčová pro procedury jako správa EPS bearerů, aktualizace oblasti sledování a další interakce s jádrem sítě, poskytuje vyhrazený kanál, který zvyšuje spolehlivost a efektivitu signalizace.

## K čemu slouží

SRB2 byl zaveden za účelem optimalizace zpracování [NAS](/mobilnisite/slovnik/nas/) signalizace poskytnutím vyhrazeného beareru odděleného od [RRC](/mobilnisite/slovnik/rrc/) zpráv, čímž se zlepšuje efektivita a spolehlivost v sítích UMTS a LTE. V časných verzích byly NAS zprávy přenášeny na SRB1, což mohlo vést k zahlcení a zpožděním jak pro řídicí, tak pro NAS signalizaci. Přesunutím NAS provozu na SRB2 po počátečním nastavení může síť lépe prioritizovat prostředky a řídit zatížení signalizace. Tím se řeší problémy jako pomalejší zřizování relací a snížená odezva pro procedury jádra sítě.

Vznik SRB2 byl motivován evolucí směrem k plně IP sítím a potřebou robustní správy relací v paketově spínaných službách. Ve verzi 8 s LTE se SRB2 stal obzvláště důležitým pro správu EPS bearerů a další funkce řízené NAS. Řeší omezení použití jediného [SRB](/mobilnisite/slovnik/srb/) pro veškerou signalizaci tím, že umožňuje paralelní zpracování a snížení kolizí. SRB2 zajišťuje, že NAS zprávy, které jsou klíčové pro interakce s jádrem sítě, mají spolehlivou a vyhrazenou cestu, čímž zlepšuje celkový výkon sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Vyhrazený bearer pro NAS zprávy po aktivaci zabezpečení
- Zřizován po navázání RRC spojení pomocí RRC rekonfigurace
- Používá potvrzovaný režim RLC pro spolehlivé doručení
- Přenáší signalizaci pro správu relací a další signalizaci jádra sítě
- Funguje souběžně se SRB1 pro oddělený signalizační provoz
- Zvyšuje efektivitu a prioritizaci pro NAS procedury

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [SRB2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/srb2/)
