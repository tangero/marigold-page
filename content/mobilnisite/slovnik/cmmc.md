---
slug: "cmmc"
url: "/mobilnisite/slovnik/cmmc/"
type: "slovnik"
title: "CMMC – Convergent Multi-Media Conference"
date: 2025-01-01
abbr: "CMMC"
fullName: "Convergent Multi-Media Conference"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cmmc/"
summary: "CMMC je služba 3GPP umožňující multimediální konferenční relace přes sítě IMS. Integruje hlasové, video a datové toky do jediné řízené konference a podporuje různé typy uživatelských terminálů a sítí."
---

CMMC je služba 3GPP umožňující multimediální konferenční hovory přes sítě IMS integrací hlasových, video a datových toků do jediné řízené relace pro bohatou skupinovou komunikaci.

## Popis

Convergent Multi-Media Conference (CMMC) je standardizovaná služba definovaná 3GPP pro multimediální konferenční hovory v rámci sítí IP Multimedia Subsystem (IMS). Poskytuje architektonický rámec a procedury pro zřizování, správu a ukončování konferencí, které kombinují více typů médií, jako je audio, video a sdílení dat (např. whiteboarding nebo přenos souborů), do jediné relace. Služba funguje nad jádrem IMS a využívá SIP (Session Initiation Protocol) pro řízení a vyjednávání relace. Využívá možnosti IMS, jako je autentizace, autorizace a správa kvality služeb (QoS), aby zajistila bezpečný a spolehlivý konferenční zážitek napříč různými přístupovými sítěmi včetně LTE, 5G NR a pevného širokopásmového připojení.

Architektura CMMC zahrnuje několik klíčových funkčních entit. Conference Focus je centrální SIP uživatelský agent, který hostuje konferenci, udržuje signalizační vztahy se všemi účastníky a mixuje nebo přepíná mediální toky. Účastníci se připojují k Conference Focus prostřednictvím svého uživatelského zařízení (UE) a jádra IMS. Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) je zodpovědná za skutečné zpracování mediálních toků, včetně mixování audia, kompozice videa a transkódování mezi různými kodeky, aby zajistila kompatibilitu mezi různorodými koncovými body. Služba interaguje s dalšími entitami IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro směrování a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data uživatelských profilů.

Z procedurálního hlediska CMMC podporuje různé modely konferencí, včetně ad-hoc konferencí vytvořených během probíhajícího hovoru a předem připravených konferencí naplánovaných dopředu. Účastník se může ke konferenci připojit prostřednictvím explicitní pozvánky (SIP INVITE) nebo vytočením URI specifického pro konferenci. Conference Focus spravuje role účastníků (např. předseda, účastník), řídí správu práva mluvit (floor control) a může podporovat funkce jako nahrávání konference a oznámení. Zpracování médií je flexibilní; například videokonference může používat centralizovaný model mixování médií, kde MRF komponuje jediné video rozložení, nebo decentralizovaný model využívající multicast nebo selektivní přeposílání.

Úloha CMMC v síti spočívá v poskytování konferenční služby na úrovni operátora (carrier-grade), která je interoperabilní a je nedílnou součástí komunikačních nabídek založených na IMS. Umožňuje poskytovatelům služeb nasazovat pokročilé konferenční funkce konzistentně napříč mobilními i pevnými sítěmi, což usnadňuje podnikové i spotřebitelské aplikace, jako jsou virtuální schůzky, webináře a společné pracovní sezení. Tím, že je CMMC součástí standardů 3GPP, zajišťuje, že implementace od různých výrobců mohou vzájemně spolupracovat, což podporuje zdravý ekosystém a bezproblémový uživatelský zážitek v síťových prostředích s více dodavateli.

## K čemu slouží

CMMC bylo vytvořeno, aby uspokojilo rostoucí poptávku po standardizovaných, síťově poskytovaných službách multimediálních konferencí v rámci architektury 3GPP typu all-IP, konkrétně IMS. Před jeho standardizací byly konferenční řešení často proprietární, izolované systémy, kterým chyběla interoperabilita mezi různými sítěmi a typy terminálů. Tato fragmentace omezovala škálovatelnost, komplikovala poskytování služeb a zhoršovala uživatelský zážitek nekonzistentními funkcemi a kvalitou. Vzestup mobilního širokopásma a konvergence pevných a mobilních sítí si vyžádaly jednotný přístup ke konferencím, který by mohl využívat řídicí a účtovací schopnosti jádra IMS.

Primární problém, který CMMC řeší, je umožnění bezproblémové, bohaté multimediální skupinové komunikace jako nativní síťové služby, nikoli jako aplikace typu over-the-top. Díky integraci do IMS může CMMC využívat síťově řízenou QoS pro garantovanou kvalitu médií, vynucovat bezpečnostní politiky prostřednictvím autentizace IMS a podporovat integrované účtování prostřednictvím Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)). To umožňuje operátorům nabízet diferencované, spolehlivé konferenční služby s obchodními modely, jako je prémiový konferenční hovor. Dále podporuje konvergenci tím, že umožňuje účastníkům připojit se z různých přístupových sítí (např. ze smartphonu 4G, tabletu 5G nebo kabelového VoIP telefonu) pomocí stejné servisní logiky.

Historicky byly multimediální konference často řešeny samostatnými systémy nebo internetovými aplikacemi, které fungovaly nezávisle na podkladové síti. Tyto přístupy neměly schopnost garantovat výkon, hluboce se integrovat s operátorskými službami (jako je překlad čísel nebo tísňové volání) nebo efektivně spravovat síťové zdroje. CMMC, představené ve 3GPP Release 8 spolu s dozráváním IMS pro mobilní sítě, poskytlo standardizovaný plán pro operátory, jak začlenit konferenční služby do svého portfolia. Vyřešilo omezení předchozích nestandardizovaných nebo přístupově specifických konferencí definováním jasné architektury, která harmonicky spolupracuje s dalšími službami IMS, jako je Voice over LTE (VoLTE) a Rich Communication Services (RCS), a zajišťuje tak konzistentní a řízený uživatelský zážitek.

## Klíčové vlastnosti

- Podpora smíšených typů médií (audio, video, data) v rámci jedné konferenční relace
- Integrace s jádrem IMS pro autentizaci, autorizaci a správu QoS
- Flexibilní modely konferencí včetně ad-hoc a předem připravených konferencí
- Centralizované zpracování médií prostřednictvím Media Resource Function (MRF) pro mixování a transkódování
- Řízení práva mluvit (floor control) a správa rolí účastníků (např. oprávnění předsedy)
- Interoperabilita napříč různorodými uživatelskými zařízeními a typy síťového přístupu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TR 22.948** (Rel-19) — IMS Convergent Multimedia Conferencing Requirements

---

📖 **Anglický originál a plná specifikace:** [CMMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmmc/)
