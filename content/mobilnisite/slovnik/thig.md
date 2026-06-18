---
slug: "thig"
url: "/mobilnisite/slovnik/thig/"
type: "slovnik"
title: "THIG – Topology Hiding Inter-network Gateway"
date: 2025-01-01
abbr: "THIG"
fullName: "Topology Hiding Inter-network Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/thig/"
summary: "Aplikační brána protokolu Session Initiation Protocol (SIP) nasazená na hranicích sítě, která skrývá interní topologii sítě před externími sítěmi IP Multimedia Subsystem (IMS). Upravuje hlavičky zpráv"
---

THIG je aplikační brána na úrovni SIP nasazená na hranicích sítě, která skrývá interní topologii IMS úpravou hlaviček zpráv SIP, čímž zvyšuje bezpečnost a důvěrnost operátora.

## Popis

Topology Hiding Inter-network Gateway (THIG) je klíčová bezpečnostní a soukromí zajišťující komponenta v architektuře IP Multimedia Subsystem (IMS), která funguje na aplikační vrstvě pro signalizaci [SIP](/mobilnisite/slovnik/sip/). Jejím hlavním úkolem je skrýt interní strukturu, adresy uzlů a topologii sítě operátora IMS před partnerskými nebo navštívenými sítěmi. Toho dosahuje tím, že funguje jako Back-to-Back User Agent ([B2BUA](/mobilnisite/slovnik/b2bua/)) nebo jako proxy SIP pro všechny mezisíťové signalizační zprávy SIP, včetně INVITE, REGISTER a MESSAGE. Když zpráva SIP prochází z interní sítě do externí sítě, THIG zkoumá a upravuje specifické hlavičky SIP.

Klíčové hlavičky určené k úpravě jsou Via, Record-Route a někdy také hlavičky Contact a Path. Primární pozornost je zaměřena na zásobník hlaviček Via, který zaznamenává cestu, kterou požadavek urazil. THIG před předáním zprávy externě odstraní interní položky Via, které obsahují privátní IP adresy nebo prozrazující doménová jména. Často je nahradí jedinou položkou Via odkazující na sebe sama, takže se jeví jako jediný vstupní bod. Podobně pro směrování budoucích požadavků v rámci dialogu může THIG upravit hlavičky Record-Route, aby se do nich vložil, a zajistil tak, že i následné zprávy v dialogu projdou přes něj za účelem skrytí topologie. THIG udržuje stav pro probíhající relace, aby správně směroval odpovědi a následné požadavky zpět k původním interním uzlům, i když jsou jejich identity skryty před externí stranou.

Architektonicky je THIG typicky nasazen na hranici sítě, často společně umístěn nebo integrován do funkce Interconnection Border Control Function ([IBCF](/mobilnisite/slovnik/ibcf/)), jak je definováno v pozdějších vydáních. Interně rozhraní s [S-CSCF](/mobilnisite/slovnik/s-cscf/) a dalšími uzly jádra IMS a s externími sítěmi přes referenční bod Mm. Jeho činnost je pro službu koncového uživatele transparentní, ale pro síťového operátora zásadní. Skrytím interních IP adres, hostname serverů a síťové architektury THIG zmírňuje bezpečnostní hrozby, jako jsou útoky založené na topologii, průzkum a zachytávání provozu cílené na specifické interní prvky. Je základním prvkem pro umožnění bezpečného partnerského propojení IMS a vzájemného propojení mezi různými administrativními doménami.

## K čemu slouží

THIG byl vytvořen, aby řešil významné bezpečnostní a provozní obavy pramenící z otevřenosti protokolu [SIP](/mobilnisite/slovnik/sip/) a vzájemného propojení IMS. Protokol SIP záměrně zahrnuje do hlaviček zpráv směrovací informace pro zajištění spolehlivého doručení. Při použití přes nedůvěryhodné administrativní hranice však tento únik informací odhaluje interní síťovou architekturu operátora – včetně počtu, typů a adres hlavních serverů, jako jsou [CSCF](/mobilnisite/slovnik/cscf/). Toto odhalení vytváří zranitelnost, která potenciálním útočníkům umožňuje zmapovat síť pro cílené útoky, jako je odepření služby (DoS) na konkrétních interních uzlech nebo zneužití známých softwarových zranitelností na odhalených typech serverů.

Zavedený ve 3GPP Release 5 s počátečními specifikacemi IMS, THIG tento problém vyřešil standardizací metody pro skrytí topologie. Před jeho definicí mohli operátoři používat obecné firewally nebo překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)), ale ty jsou nedostatečné pro aplikační protokoly jako SIP, kde jsou směrovací informace vloženy do datové části. THIG poskytuje řešení citlivé na aplikaci. Jeho vývoj byl motivován komerční potřebou operátorů udržet své síťové investice a konfigurace důvěrnými, a přitom se stále účastnit globální interoperability multimediálních služeb.

THIG navíc podporuje regulatorní a obchodní požadavky na důvěrnost vzájemného propojení. Umožňuje operátorům partnersky spolupracovat s konkurenty, aniž by odhalovali kapacitní nebo architektonické detaily, které by mohly být použity pro konkurenční analýzu. Jak se IMS vyvinulo v jádro pro VoLTE a VoNR, role THIG se stala ještě kritičtější pro zabezpečení hlasové a messagingové infrastruktury, což zajišťuje, že přechod na plně IP sítě nepřinesl snížení síťové bezpečnosti a důvěrnosti operátora.

## Klíčové vlastnosti

- Funguje jako SIP Back-to-Back User Agent (B2BUA) nebo proxy pro skrytí topologie
- Selektivně odstraňuje nebo upravuje hlavičky Via, Record-Route a Contact v zprávách SIP
- Udržuje stav relace pro zajištění správného směrování zpráv v rámci dialogu
- Skrývá interní IP adresy uzlů, hostname a topologii sítě před externími sítěmi
- Typicky integrován s funkcí Interconnection Border Control Function (IBCF)
- Chrání před útoky na zjištění topologie a zvyšuje bezpečnost vzájemného propojení

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 32.849** (Rel-13) — IMS Roaming Charging Study

---

📖 **Anglický originál a plná specifikace:** [THIG na 3GPP Explorer](https://3gpp-explorer.com/glossary/thig/)
