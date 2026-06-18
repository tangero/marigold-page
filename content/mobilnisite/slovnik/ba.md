---
slug: "ba"
url: "/mobilnisite/slovnik/ba/"
type: "slovnik"
title: "BA – Bandwidth Adaptation"
date: 2025-01-01
abbr: "BA"
fullName: "Bandwidth Adaptation"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ba/"
summary: "Bandwidth Adaptation (BA) je mechanismus 3GPP umožňující dynamické přizpůsobení přenosové šířky pásma přidělené uživatelskému zařízení (UE) podle požadavků provozu a rádiových podmínek. Optimalizuje v"
---

BA je mechanismus 3GPP, který dynamicky upravuje přenosovou šířku pásma UE na základě provozu a rádiových podmínek za účelem optimalizace využití zdrojů, snížení spotřeby energie a zlepšení spektrální účinnosti.

## Popis

Bandwidth Adaptation (BA) je sofistikovaná technika správy rádiových zdrojů definovaná ve standardech 3GPP, primárně pro New Radio (NR) v systémech 5G. Umožňuje uživatelskému zařízení (UE) dynamicky přepínat mezi různými částmi šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)) nakonfigurovanými v rámci celkové šířky kanálu nosné. BWP je souvislá sada bloků fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)), která definuje podmnožinu celkové šířky pásma nosné. Síť (gNB) konfiguruje pro UE více BWP prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), každé s konkrétními parametry, jako je numerologie (rozteč subnosných, cyklická předpona), šířka pásma a frekvenční umístění. UE poté pracuje v rámci jednoho aktivního BWP najednou pro uplink i downlink, s možností přepínat na základě explicitních příkazů ([DCI](/mobilnisite/slovnik/dci/)) od gNB nebo po vypršení časovače (BWP-InactivityTimer).

Jádrovou architektonickou složkou umožňující BA je rámec konfigurace a přepínání BWP v rámci protokolového zásobníku NR. Vrstva [MAC](/mobilnisite/slovnik/mac/) gNB spravuje aktivaci a deaktivaci BWP. Když má UE nízkou datovou aktivitu, gNB může nařídit přepnutí na užší BWP, čímž šetří energii baterie UE, protože rádiové frekvenční komponenty (jako výkonový zesilovač a analogově-digitální převodníky) mohou pracovat v redukované šířce pásma, což snižuje odběr energie. Naopak při příchodu dat s vysokou propustností gNB rychle přepne UE na širší BWP, aby pokryl poptávku. K tomuto přepínání dochází s minimální latencí, často během několika slotů, což zajišťuje plynulou kontinuitu služby.

BA funguje ve spojení s dalšími funkcemi NR, jako je škálovatelná numerologie a indikace formátu slotu. Různá BWP mohou být konfigurována s různými numerologiemi (např. 15 kHz [SCS](/mobilnisite/slovnik/scs/) pro širokoplošné pokrytí a 60 kHz SCS pro služby s nízkou latencí), což umožňuje přizpůsobení jak šířky pásma, tak charakteristik v časové oblasti. Plánovač gNB hraje klíčovou roli, když rozhoduje o optimálním BWP pro každé UE na základě stavu vyrovnávací paměti, ukazatelů kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), požadavků kvality služby (QoS) aktivních datových rádiových nosičů a celkového zatížení buňky. Toto dynamické přizpůsobení je zásadní pro efektivní multiplexování různorodých typů provozu (např. massive IoT, enhanced mobile broadband, ultra-reliable low-latency communications) na stejné nosné.

Z pohledu UE BA zjednodušuje [RF](/mobilnisite/slovnik/rf/) návrh a snižuje náklady a spotřebu energie. Namísto toho, aby vyžadovala RF komponenty schopné nepřetržitého zpracování celé šířky pásma nosné (která může být až 400 MHz v pásmu FR2 a 100 MHz v pásmu FR1), může být UE navržena pro maximální podporovanou šířku BWP. UE monitoruje řídicí kanály (PDCCH) pouze v rámci svého aktivního BWP, což dále šetří energii. BA je tedy základním prvkem umožňujícím široké šířky pásma nosných v 5G NR, díky čemuž jsou prakticky použitelné pro zařízení s různými schopnostmi a požadavky služeb, aniž by byla obětována účinnost nebo výkon.

## K čemu slouží

Bandwidth Adaptation byl vytvořen, aby řešil základní výzvy spojené s extrémně širokými šířkami kanálů podporovanými v 5G New Radio (až 100 MHz v pásmech pod 6 GHz a 400 MHz v mmWave pásmech). Nepřetržitý provoz rádiového frekvenčního (RF) řetězce UE v celé šířce pásma nosné je vysoce neefektivní z hlediska spotřeby energie, zejména pro zařízení s omezenou kapacitou baterie, jako jsou chytré telefony a IoT senzory. BA to řeší tím, že umožňuje síti dynamicky přizpůsobit provozní šířku pásma UE jeho okamžitým potřebám propustnosti dat, což dramaticky snižuje spotřebu energie během období nízké aktivity.

Historicky, v LTE, byla šířka pásma kanálu UE z velké části statická, svázaná s její výkonnostní třídou. Přechod k flexibilnější, na služby orientované architektuře 5G vyžadoval agilnější přístup. BA byla motivována potřebou podporovat mnohem širší škálu případů užití – od gigabitové enhanced mobile broadband (eMBB) po sporadické přenosy malých paketů od IoT zařízení – na stejné infrastruktuře. Bez BA by obsluha zařízení s nízkou datovou rychlostí na širokopásmové nosné byla spektrálně a energeticky plýtvavá, protože by zabírala zbytečné RF zdroje a vyčerpávala jejich baterie.

BA navíc řeší praktická omezení RF implementace UE. Návrh dostupných, energeticky efektivních RF komponent (jako výkonové zesilovače a filtry), které mohou lineárně pracovat v rozsahu několika set megahertz, je náročný. BA umožňuje výrobcům UE navrhovat zařízení pro rozumnější maximální okamžitou šířku pásma, čímž snižuje náklady a složitost. Poskytuje také síťovým operátorům mocný nástroj pro správu rádiových zdrojů, umožňuje efektivní multiplexování heterogenního provozu a optimalizuje celkovou kapacitu buňky a uživatelský zážitek přidělováním šířky pásma přesně tam a tehdy, kde a kdy je potřeba.

## Klíčové vlastnosti

- Dynamické přepínání mezi nakonfigurovanými částmi šířky pásma (BWP)
- Snížení spotřeby energie UE provozem v úzkém pásmu během nečinnosti
- Podpora více numerologií (roztečí subnosných) na BWP
- Přepínání BWP spouštěno prostřednictvím downlink control information (DCI) nebo časovače BWP-InactivityTimer
- Nezávislá konfigurace uplink a downlink BWP
- Umožňuje efektivní podporu širokých šířek pásma nosných pro různorodé schopnosti UE

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.828** (Rel-10) — Study on 3GPP-TMF NRM/SID Alignment
- **TS 32.829** (Rel-10) — Fault Management Alignment Study
- **TS 32.831** (Rel-10) — 3GPP-TMF PM Alignment Study
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [BA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ba/)
