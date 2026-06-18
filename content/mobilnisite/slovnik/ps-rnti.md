---
slug: "ps-rnti"
url: "/mobilnisite/slovnik/ps-rnti/"
type: "slovnik"
title: "PS-RNTI – Power Saving Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "PS-RNTI"
fullName: "Power Saving Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ps-rnti/"
summary: "UE-specifický RNTI zavedený v 5G NR pro umožnění úspory energie. Používá ho gNB k plánování a vysílání signálů a příkazů pro úsporu energie k UE ve stavu RRC_CONNECTED, což UE umožňuje vstupovat do mi"
---

PS-RNTI je uživatelskému zařízení (UE) specifický dočasný identifikátor rádiové sítě používaný v 5G NR pro plánování signálů a příkazů pro úsporu energie, který umožňuje připojeným UE vstupovat do mikro-spánků a snižovat spotřebu energie.

## Popis

Power Saving [RNTI](/mobilnisite/slovnik/rnti/) (PS-RNTI) je klíčový identifikátor v protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) pro 5G New Radio (NR), specificky definovaný pro vylepšení Connected Mode Discontinuous Reception (C-DRX). Jedná se o 16bitový identifikátor, podobně jako jiné RNTI, který je však uživatelskému zařízení (UE) jedinečně přiřazen gNodeB (gNB) za účelem usnadnění pokročilých mechanismů úspory energie. Primární funkcí PS-RNTI je umožnit gNB odesílat specifické formáty řídicích informací pro downlink ([DCI](/mobilnisite/slovnik/dci/)) pro úsporu energie, které nesou příkazy nebo indikace instruující UE k úpravě aktivity svého přijímače.

Z architektonického hlediska PS-RNTI funguje v rámci vrstev [MAC](/mobilnisite/slovnik/mac/) a RRC. gNB nakonfiguruje UE s hodnotou PS-RNTI pomocí signalizace RRC. Následně může gNB vysílat formát DCI 2_6, který je skramblován pomocí PS-RNTI, na vyhrazeném fyzickém řídicím kanálu pro úsporu energie (PS-PDCCH) nebo v nakonfigurovaném prohledávacím prostoru. UE toto DCI monitoruje během svých nakonfigurovaných časovačů "On Duration" v rámci cyklu C-DRX. Datová část DCI obsahuje indikaci Wake-Up Signalu ([WUS](/mobilnisite/slovnik/wus/)) nebo signálu Go-To-Sleep. WUS informuje UE, že jsou v nadcházejícím [DRX](/mobilnisite/slovnik/drx/) cyklu naplánována downlink data, a UE by tedy mělo zůstat vzhůru. Naopak signál Go-To-Sleep říká UE, že žádná data nečekají, což mu umožňuje zcela vynechat další On Duration a vstoupit do hlubšího stavu spánku.

Úlohou tohoto mechanismu je oddělit povinná monitorovací období UE od skutečného plánování dat. Bez PS-RNTI se musí UE v C-DRX probouzet pro každé On Duration, aby zkontrolovalo plánovací povolení, i když žádná data nejsou přítomna, což plýtvá energií. S PS-RNTI a DCI 2_6 může gNB dynamicky instruovat UE, aby vynechalo zbytečná probuzení, což výrazně prodlužuje životnost baterie. PS-RNTI je tedy klíčovým prvkem pro provoz s ultra-spolehlivým nízkým příkonem, který vyžaduje mnoho 5G případů užití, včetně massive IoT a enhanced mobile broadband pro ruční zařízení. Jeho provoz je těsně integrován s dalšími RNTI, jako je [C-RNTI](/mobilnisite/slovnik/c-rnti/) (pro běžné plánování) a [SI-RNTI](/mobilnisite/slovnik/si-rnti/) (pro systémové informace), ale slouží specifickému účelu správy spotřeby energie.

## K čemu slouží

PS-RNTI byl vytvořen, aby řešil kritickou výzvu vysoké spotřeby energie pro zařízení 5G NR, zejména smartphony a IoT senzory, pracující v připojeném stavu. Bylo zjištěno, že raná nasazení 5G, s širšími šířkami pásma a složitějšími operacemi MIMO (multiple-input multiple-output), vybíjela baterie zařízení rychleji než 4G. Tradiční mechanismy C-DRX, ač užitečné, byly neefektivní, protože se UE muselo periodicky probouzet a dekódovat PDCCH během každého On Duration, čímž spotřebovávalo energii i když nebyla naplánována žádná data.

Motivací pro PS-RNTI bylo zavést inteligentnější a dynamičtější řízení spánku. Řeší problém povinných periodických probuzení tím, že umožňuje síti poskytovat explicitní instrukce. To umožňuje příležitosti pro "mikro-spánek" v rámci připojeného stavu, což byl koncept v LTE méně propracovaný. Historickým kontextem je pracovní položka 3GPP Rel-16 "NR UE Power Saving", jejímž cílem bylo identifikovat a standardizovat techniky pro zlepšení životnosti baterie bez kompromisů v latenci nebo propustnosti. PS-RNTI spolu s přidruženým Wake-Up Signálem (WUS) byl klíčovým řešením, které umožnilo síti přesně řídit aktivitu UE a snížit plýtvání energií způsobené slepým monitorováním, čímž se prodloužila provozní doba zařízení s omezenou kapacitou baterie.

## Klíčové vlastnosti

- Umožňuje přenos specifického formátu DCI 2_6 pro úsporu energie
- Umožňuje gNB odesílat Wake-Up Signály (WUS) připojeným UE
- Umožňuje gNB odesílat příkazy Go-To-Sleep připojeným UE
- Snižuje spotřebu energie UE umožněním vynechání DRX On Duration
- UE-specifická konfigurace prostřednictvím signalizace RRC
- Funguje v rámci vylepšeného frameworku Connected Mode DRX (C-DRX)

## Související pojmy

- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PS-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ps-rnti/)
