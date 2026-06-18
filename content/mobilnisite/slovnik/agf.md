---
slug: "agf"
url: "/mobilnisite/slovnik/agf/"
type: "slovnik"
title: "AGF – Access Gateway Function"
date: 2025-01-01
abbr: "AGF"
fullName: "Access Gateway Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/agf/"
summary: "Access Gateway Function (AGF) je komponenta jádra sítě 5G, která zajišťuje přístup přes pevné sítě. Propojuje zařízení na straně zákazníka (CPE) přes pevné širokopásmové připojení s jádrem sítě 5G a u"
---

AGF je komponenta jádra sítě 5G, která propojuje zařízení na straně zákazníka (CPE) přes pevné širokopásmové připojení s jádrem sítě 5G a umožňuje konvergované služby pevných a mobilních sítí.

## Popis

Access Gateway Function (AGF) je funkční prvek uvnitř jádra sítě 5G (5GC), konkrétně definovaný pro podporu drátového přístupu (Wireline Access). Jeho hlavní rolí je fungovat jako brána a řídicí bod pro uživatelská zařízení (UE) připojená přes pevné širokopásmové sítě, jako jsou sítě využívající Digital Subscriber Line ([DSL](/mobilnisite/slovnik/dsl/)), kabelové přípojky nebo optická vlákna. AGF ukončuje přístupově specifické protokoly od zařízení na straně zákazníka ([CPE](/mobilnisite/slovnik/cpe/)) a prezentuje standardizované rozhraní ([N2](/mobilnisite/slovnik/n2/) a N3) směrem k funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a k funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) jádra 5G. To umožňuje jádru 5G spravovat relace a mobilitu těchto pevně připojených zařízení, jako by byla připojena přes 3GPP rádiovou přístupovou síť, čímž umožňuje skutečnou konvergenci pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)).

Architektonicky se AGF nachází na hranici mezi nedůvěryhodnou přístupovou sítí mimo 3GPP (pevné širokopásmové připojení) a důvěryhodným jádrem 5G. Obsahuje jak funkce řídicí roviny, tak uživatelské roviny. Na řídicí rovině komunikuje s AMF přes rozhraní N2 pro procedury registrace, autentizace a správy mobility. Také komunikuje s funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) pro správu politik a relací, často prostřednictvím AMF. Na uživatelské rovině se AGF připojuje k UPF přes rozhraní N3 a vytváří datovou cestu pro uživatelský provoz. AGF zajišťuje zapouzdření a rozbalení uživatelských dat, typicky využívající protokoly jako Point-to-Point Protocol over Ethernet (PPPoE) nebo IP přes pevný okruh, a mapuje tyto toky na příslušné relace paketových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)) uvnitř systému 5G.

Klíčové vnitřní komponenty AGF zahrnují ukončovací bod pro protokoly pevných linek (např. funkci Broadband Network Gateway (BNG)), bezpečnostní funkce pro počáteční autentizaci a šifrování spoje a logiku pro mapování přístupově specifických parametrů (jako identifikátory linky) na identifikátory jádra 5G (jako SUPI a GPSI). Plní podobnou roli jako Trusted Non-3GPP Interworking Function (TNGF), ale je specificky optimalizována pro charakteristiky a požadavky drátového přístupu, který je typicky považován za stabilnější a s vyšší propustností než bezdrátový přístup mimo 3GPP. Činnost AGF se řídí politikami od funkce řízení politik (PCF), což zajišťuje konzistentní vynucování kvality služeb a přístupových pravidel napříč různými typy přístupu.

Tím, že abstrahuje detaily pevného přístupu, umožňuje AGF operátorům využít jejich stávající širokopásmovou infrastrukturu k poskytování služeb 5G. To zahrnuje nejen vylepšené mobilní širokopásmové služby, ale také síťové segmenty (network slicing) a služby s nízkou latencí pro pevná místa. AGF zajišťuje, že funkce jako plynulá mobilita mezi pevným a mobilním přístupem, konzistentní autentizace a jednotné vynucování politik se stanou realitou, čímž tvoří základní kámen konvergované architektury jádra 5G.

## K čemu slouží

Access Gateway Function byla vytvořena jako odpověď na trend směřující ke konvergenci pevných a mobilních sítí (FMC) v rámci systému 5G. Před 5G fungovaly pevné a mobilní sítě do značné míry jako oddělené sila s odlišnými jádry sítí (např. IMS pro pevnou telefonii, EPC pro mobilní). Toto oddělení vedlo k provozní neefektivitě, duplikaci funkcí a neschopnosti nabízet skutečně jednotné služby fungující bezproblémově napříč oběma typy přístupu. Architektura jádra 5G byla navržena od počátku jako přístupově agnostická, ale pro integraci rozsáhlé instalované základny pevných širokopásmových sítí byl potřeba standardizovaný a efektivní bránový prvek.

AGF řeší konkrétní problém, jak připojit starší pevné přístupové sítě, které používají protokoly jako PPPoE, DHCP nebo IPoE, do cloud-nativní, službami založené architektury jádra 5G. Bez AGF by operátoři potřebovali složitá a proprietární propojovací řešení. AGF poskytuje standardizovanou metodu definovanou 3GPP pro autentizaci účastníků pevných linek pomocí přihlašovacích údajů 5G (jako 5G-AKA), navazování zabezpečených relací PDU pro ně a aplikaci řízení kvality služeb (QoS) a politik 5G na jejich provoz. To umožňuje operátorům modernizovat jejich pevné sítě využitím pokročilých schopností jádra 5G, jako jsou síťové segmenty pro podnikové služby nebo edge computing, aniž by museli nahrazovat infrastrukturu poslední míle.

Historicky byly pevné širokopásmové sítě spravovány Broadband Network Gateway (BNG) v kontextu IP Multimedia Subsystem (IMS) nebo jednoduchých IP služeb. Vývoj AGF uznává, že inteligence a správa relací by pro konvergované služby měly sídlit v mobilním jádře. Vytvoření AGF ve specifikaci 3GPP Release 16 bylo motivováno snahou sjednotit poskytování služeb, snížit provozní náklady a vytvořit nové zdroje příjmů prostřednictvím kombinovaných nabídek pevných a mobilních služeb. Odstraňuje omezení předchozích přístupů s duální architekturou tím, že poskytuje jediné, jednotné jádro pro všechny typy přístupu, což umožňuje konzistentní uživatelský zážitek a zjednodušenou správu.

## Klíčové vlastnosti

- Ukončuje protokoly pevného širokopásmového přístupu (např. PPPoE, IPoE) a provádí jejich propojení na rozhraní 5G N2/N3
- Umožňuje autentizaci zařízení na pevných linkách pomocí 5G-AKA a přihlašovacích údajů účastníka 5G
- Podporuje navazování a správu relací PDU pro UE přes drátový přístup mimo 3GPP
- Mapuje identifikátory pevných přístupových linek na identifikátory předplatného 5G (SUPI/GPSI)
- Aplikuje politiky kvality služeb 5G a pravidla účtování přijatá od PCF na provoz z pevného přístupu
- Umožňuje plynulou kontinuitu služeb a konzistenci politik napříč pevným a 3GPP mobilním přístupem

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [AGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/agf/)
