---
slug: "pfm"
url: "/mobilnisite/slovnik/pfm/"
type: "slovnik"
title: "PFM – Packet Flow Management"
date: 2025-01-01
abbr: "PFM"
fullName: "Packet Flow Management"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pfm/"
summary: "Packet Flow Management (PFM, správa toků paketů) je soubor procedur a protokolů v jádrových sítích GSM/EDGE a GPRS pro zřizování, modifikaci a uvolňování kontextů paketových dat a s nimi spojených pře"
---

PFM je soubor procedur a protokolů v sítích GSM/EDGE a GPRS pro zřizování, modifikaci a uvolňování kontextů paketových dat a přenosových kanálů mezi mobilní stanicí a sítí.

## Popis

Packet Flow Management (PFM, správa toků paketů) je klíčový funkční proces v architektuře paketově spínaných sítí 2G (GSM/[EDGE](/mobilnisite/slovnik/edge/)) a 2.5G ([GPRS](/mobilnisite/slovnik/gprs/)). Zahrnuje signalizační procedury a související protokoly používané k řízení zřizování, modifikace a ukončování přenosových prostředků pro paketová data, známých jako toky paketů (Packet Flows) nebo kontexty [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol), mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a síťovým uzlem [SGSN](/mobilnisite/slovnik/sgsn/) (Serving GPRS Support Node). Tok paketů představuje logickou komunikační cestu se specifickými atributy kvality služby (QoS) pro přenos paketů uživatelských dat. Procedury PFM se primárně provádějí pomocí protokolů GPRS Mobility Management a Session Management ([GMM/SM](/mobilnisite/slovnik/gmm-sm/)) přes rozhraní rádiového přístupu a pomocí řídicí složky GPRS Tunneling Protocol ([GTP-C](/mobilnisite/slovnik/gtp-c/)) v jádrové síti.

Proces začíná iniciací procedury aktivace kontextu PDP ze strany MS, což je klíčová funkce PFM. Tento požadavek, odeslaný do SGSN, obsahuje požadované parametry QoS. SGSN následně interaguje s uzlem GGSN (Gateway GPRS Support Node) prostřednictvím GTP-C za účelem vytvoření [GTP](/mobilnisite/slovnik/gtp/) tunelu a zřízení koncového přenosového kanálu. SGSN také koordinuje s rádiovou přístupovou sítí (BSS) přidělení potřebných rádiových prostředků (dočasných blokových toků) na rozhraní Um. Rámec PFM definuje konkrétní toky zpráv a časovače (jako jsou Packet Flow Timers, PFT) pro správu stavu těchto kontextů. Například procedura modifikace kontextu PDP iniciovaná sítí umožňuje dynamické přizpůsobení QoS během aktivní relace, zatímco procedura deaktivace uvolní všechny přidružené prostředky.

PFM funguje ve spolupráci s dalšími rovinami správy, jako je správa mobility (MM) a správa rádiových prostředků (RR). Je zodpovědná za správu více souběžných toků paketů pro jednu MS, z nichž každý může mít odlišný profil QoS, což umožňuje služby jako simultánní prohlížení webu a VoIP. SGSN funguje jako centrální řadič pro PFM, udržuje stavy kontextů PDP, vynucuje QoS a spravuje mapování mezi logickými kontexty PDP MS a fyzickými přenosovými kanály v rádiové a jádrové síti. Tato správa je klíčová pro efektivní využití prostředků, podporu různých tříd provozu (konverzační, streamovací, interaktivní, na pozadí) a poskytuje základ pro mobilní internetové připojení v sítích před 3G.

## K čemu slouží

Packet Flow Management byl vytvořen za účelem zavedení a správy paketově spínaných datových služeb v původně pouze okruhově spínané síti GSM. Před GPRS podporoval GSM data prostřednictvím okruhově spínaných datových hovorů, které byly pro přerušovaný internetový provoz neefektivní, protože na celou dobu relace vyčlenily celý časový slot. Vývoj GPRS vyžadoval nový paradigma pro správu prostředků, které by dokázalo zvládnout 'vždy připojenou' konektivitu, dynamické přidělování prostředků a více paralelních datových relací s různými požadavky na kvalitu.

PFM vyřešil kritický problém zřizování a řízení 'virtuálních spojení' neboli přenosových kanálů pro paketová data. Poskytl nezbytný signalizační rámec pro nastavení kontextu PDP – základního konceptu, který váže IP adresu MS ke konkrétnímu profilu QoS a GTP tunelu směrem k GGSN. To byl radikální odklon od trvalých okruhově spínaných spojení. PFM umožnil síti přidělovat rádiové a jádrové prostředky na základě jednotlivých paketů (v blocích) namísto vyčleňování nepřetržitého kanálu, což dramaticky zlepšilo spektrální účinnost pro data. Jeho procedury pro modifikaci a deaktivaci umožnily síti přizpůsobit se měnícím se potřebám uživatele a efektivně získávat prostředky zpět, což bylo zásadní pro škálování raných mobilních datových služeb. PFM položil základní stavební kameny pro koncepty vyvinutého paketového jádra, které se později objevily v 3G UMTS a 4G LTE.

## Klíčové vlastnosti

- Spravuje životní cyklus kontextů PDP (aktivace, modifikace, deaktivace)
- Využívá signalizaci GMM/SM přes rádiové rozhraní a GTP-C v jádru sítě
- Koordinuje přidělování prostředků mezi MS, BSS, SGSN a GGSN
- Podporuje více souběžných toků paketů s nezávislými profily QoS
- Umožňuje dynamické vyjednávání a modifikaci QoS během relace
- Definuje a používá časovače toků paketů (PFT) pro správu stavu a prostředků

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)

## Definující specifikace

- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [PFM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pfm/)
