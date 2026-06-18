---
slug: "e-ggsn"
url: "/mobilnisite/slovnik/e-ggsn/"
type: "slovnik"
title: "E-GGSN – Enhanced Gateway GPRS Support Node"
date: 2025-01-01
abbr: "E-GGSN"
fullName: "Enhanced Gateway GPRS Support Node"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-ggsn/"
summary: "Vylepšená verze uzlu GGSN, což je uzel v paketově spínané jádrové síti 2G/3G. Slouží jako brána mezi sítí GPRS/UMTS a externími paketovými datovými sítěmi, jako je internet. Spravuje přidělování IP ad"
---

E-GGSN je vylepšená verze uzlu Gateway GPRS Support Node, což je brána mezi sítí GPRS/UMTS a externími paketovými datovými sítěmi, která spravuje IP adresy, směrování a vynucování politik.

## Popis

Enhanced Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (E-GGSN) je klíčová komponenta v architektuře paketově spínané jádrové sítě 3GPP, konkrétně pro systémy GPRS a UMTS. Funguje jako hlavní rozhraní a brána mezi vnitřní sítí mobilního operátora a externími paketovými datovými sítěmi ([PDN](/mobilnisite/slovnik/pdn/)), jako je veřejný internet, firemní intranety nebo služby IP Multimedia Subsystem (IMS). Architektonicky se nachází v jádrové síti a je propojen se Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) přes rozhraní Gn/Gp a s externími sítěmi přes rozhraní Gi. Jeho činnost zahrnuje správu životního cyklu kontextů Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)), což jsou logické datové relace zřízené pro uživatelské zařízení (UE). Když UE zahájí datovou relaci, SGSN komunikuje s E-GGSN za účelem vytvoření PDP kontextu. E-GGSN je odpovědný za přidělení IP adresy UE (často prostřednictvím [DHCP](/mobilnisite/slovnik/dhcp/) nebo z místního fondu), autentizaci relace (často ve spolupráci se servery [AAA](/mobilnisite/slovnik/aaa/)) a vynucování politik kvality služeb (QoS) a tarifních pravidel na základě profilu účastníka. Plní klíčové síťové funkce, jako je směrování uživatelských IP paketů mezi UE a externí sítí, aplikování policingu a tvarování provozu a generování podrobných záznamů o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro účely fakturace. Často také integruje funkce firewallu a hluboké kontroly paketů (DPI) pro zabezpečení a rozpoznání služeb. Jeho role je zásadní pro umožnění mobilního širokopásmového přístupu k internetu a zajištění bezpečného a spravovatelného připojení.

## K čemu slouží

E-GGSN byl zaveden pro rozšíření schopností standardního GGSN definovaného v dřívějších vydáních 3GPP. Hlavním motivem byla podpora rostoucích nároků mobilních datových služeb, které vyžadovaly sofistikovanější zpracování provozu, lepší správu QoS a vylepšené účtovací mechanismy. Jak se mobilní sítě vyvíjely od základního [GPRS](/mobilnisite/slovnik/gprs/) k podpoře vyšších rychlostí UMTS a nakonec HSPA, jednoduché bránové funkce původního GGSN se staly nedostatečnými. Vylepšená verze byla navržena tak, aby řešila omezení v škálovatelnosti, diferenciaci služeb a integraci s vyvíjejícími se síťovými architekturami, jako je IMS. Řešila problémy spojené s obsluhou různorodých datových služeb (např. streaming, VoIP, prohlížení) s odlišnými požadavky na latenci a šířku pásma tím, že poskytovala podrobnější řízení politik a účtování (PCC). Také usnadňovala zavedení názvů přístupových bodů (APN) pro konkrétní služby a vylepšovala bezpečnostní funkce pro propojení s nedůvěryhodnými externími sítěmi. Historicky bylo jeho vytvoření součástí širšího úsilí 3GPP o přechod mobilních sítí z primárně okruhově spínaných přenašečů hlasu na robustní, plně IP paketově spínané platformy schopné poskytovat širokou škálu multimediálních služeb.

## Klíčové vlastnosti

- Správa PDP kontextů pro zřizování a ukončování mobilních datových relací
- Přidělování a správa IP adres pro uživatelské zařízení (UE)
- Vynucování politik a správa QoS na základě profilů účastníků
- Generování záznamů o účtování (CDR) pro fakturaci
- Směrovací a bránová funkce mezi mobilním jádrem a externími IP sítěmi
- Integrace s architekturou Policy and Charging Control (PCC) pro pokročilé řízení služeb

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [E-GGSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-ggsn/)
