---
slug: "cag"
url: "/mobilnisite/slovnik/cag/"
type: "slovnik"
title: "CAG – Closed Access Group"
date: 2026-01-01
abbr: "CAG"
fullName: "Closed Access Group"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cag/"
summary: "Uzavřená přístupová skupina (CAG) je funkce 5G umožňující omezený přístup k síti autorizovaným uživatelům, jako jsou zaměstnanci podniku, v konkrétní lokalitě, například v areálu nebo továrně. Zajišťu"
---

CAG je funkce 5G, která poskytuje omezený a zabezpečený přístup k síti výhradně autorizovaným uživatelům v určité lokalitě, například v podnikovém areálu.

## Popis

Uzavřená přístupová skupina (CAG) je mechanismus definovaný 3GPP v systémech 5G, který umožňuje řízený a omezený přístup k síti pro definovanou skupinu uživatelských zařízení (UE) v konkrétní geografické oblasti, jako je podnikový areál, továrna nebo nemocnice. Funguje tak, že se jeden nebo více identifikátorů CAG (CAG ID) asociuje s konkrétními buňkami, označovanými jako CAG buňky, které jsou součástí veřejné pozemní mobilní sítě (PLMN). K odpovídajícím CAG buňkám mají povolen přístup pouze ta UE, která jsou k příslušnému CAG ID předplacena a explicitně autorizována. Tím vzniká logický, přístupově řízený síťový řez v rámci veřejné infrastruktury 5G, který zajišťuje, že rádiové prostředky a síťové služby jsou vyhrazeny autorizované skupině, a zabraňuje tak neoprávněnému veřejnému přístupu.

Architektura zahrnuje několik klíčových síťových funkcí. Funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) hraje ústřední roli při vynucování řízení přístupu CAG během procedur registrace a služebního požadavku. Správa jednotných dat ([UDM](/mobilnisite/slovnik/udm/)) ukládá předplatitelská data CAG účastníka včetně seznamu povolených CAG ID pro každé UE. Tato předplatitelská data jsou poskytována AMF prostřednictvím autentizační serverové funkce ([AUSF](/mobilnisite/slovnik/ausf/)) během ověřování. Rádiová přístupová síť (RAN), konkrétně gNB, vysílá v systémovém informačním bloku 1 (SIB1) podporovaná CAG ID pro buňku pomocí parametru `cag-IdentityList`. UE nakonfigurované pro přístup CAG tyto informace vyhledává a pokusí se vybrat nebo se připojit k buňce pouze v případě, že její předplacený seznam povolených CAG obsahuje jedno z ID vysílaných touto buňkou.

Operační tok začíná u UE, která musí mít USIM obsahující seznam řízení přístupu specifický pro CAG. Když je UE zapnuta nebo vstoupí do oblasti, přečte si seznam CAG ID z SIB1 buňky. UE tento seznam porovná se svým uloženým seznamem povolených CAG. Pokud najde shodu, pokračuje UE procedurou počáteční registrace a oznámí síti svůj vybraný CAG ID. AMF následně ověří autorizaci UE kontrolou předplatitelských dat přijatých od UDM. Pokud UE není pro požadovaný CAG autorizována, AMF registraci odmítne s příslušným kódem příčiny, například "CAG not allowed". Při mobilitě obecně není UE povoleno provést předání spojení (handover) do CAG buňky, pokud pro tento CAG není autorizováno, čímž je zajištěno, že uzavřený charakter skupiny je zachován i během pohybu.

CAG je úzce integrována s dalšími funkcemi 5G, jako je síťové řezání (Network Slicing). CAG může být asociována s jednou nebo více instancemi síťových řezů (NSI), což umožňuje uzavřené skupině uživatelů přístup ke specifickým, na míru šitým službám (např. ultra-spolehlivá nízkolatenční komunikace pro tovární automatizaci) na vyhrazené logické síti. Tato kombinace poskytuje jak řízení přístupu, tak izolaci služeb. Správu a vystavení možností CAG zajišťuje funkce vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) a funkce vystavení servisních schopností (SCEF) pro northbound [API](/mobilnisite/slovnik/api/), což umožňuje podnikovým aplikacím spravovat členství v CAG a příslušné politiky.

## K čemu slouží

CAG byla představena ve 3GPP Release 16, aby reagovala na rostoucí poptávku vertikálních odvětví (např. výroba, energetika, zdravotnictví) a podniků po soukromém, zabezpečeném a řízeném přístupu k síti 5G. Před CAG existovaly podobné koncepty, jako uzavřené skupiny účastníků ([CSG](/mobilnisite/slovnik/csg/)) v 4G LTE, které byly primárně navrženy pro rezidenční femtobuňky. CSG však měly omezení pro rozsáhlá podniková nasazení, včetně méně flexibilní správy předplatného a omezené integrace s moderními principy 5G jádra sítě, jako je síťové řezání a architektura založená na službách. CAG byla vytvořena, aby poskytla škálovatelnější, politikami řízený a na síťové řezy navázaný mechanismus řízení přístupu vhodný pro profesionální a průmyslové případy užití.

Hlavním problémem, který CAG řeší, je umožnění veřejnému síťovému operátorovi nabídnout zážitek "virtuální privátní sítě" na sdílené veřejné RAN a jádrové infrastruktuře. Bez CAG by podnik potřeboval fyzicky oddělenou, vyhrazenou síť (skutečnou privátní síť), aby zajistil, že se mohou připojit pouze jeho zařízení, což je nákladné a neefektivní. CAG umožňuje operátorovi logicky oddělit část své veřejné sítě a určit určité buňky pro výhradní použití autorizovanými zařízeními zákazníka. Tím se řeší problémy neoprávněného přístupu, soupeření o rádiové prostředky s veřejnými uživateli a nedostatku záruk služeb pro kritické podnikové aplikace.

Dále CAG podporuje vizi 5G "síť jako služba" a síťového řezání tím, že poskytuje základní vrstvu řízení přístupu. Umožňuje podnikům mít garantované připojení pro jejich kritická IoT zařízení, autonomní vozíky a nástroje [AR](/mobilnisite/slovnik/ar/)/VR bez rušení veřejným provozem. Motivace vychází z trendů digitalizace průmyslu (Průmysl 4.0), kde je spolehlivé, nízkolatenční a zabezpečené bezdrátové připojení nezbytností. CAG v kombinaci se síťovým řezáním umožňuje operátorům plnit přísné smlouvy o úrovni služeb (SLA) pro tyto vertikální zákazníky na sdílené infrastruktuře, čímž otevírá nové zdroje příjmů a případy užití přesahující tradiční mobilní širokopásmový přístup pro spotřebitele.

## Klíčové vlastnosti

- Omezuje přístup k síti pouze na UE s explicitním předplatným pro konkrétní identifikátor CAG
- Identifikátory CAG jsou vysílány gNB v SIB1, což umožňuje UE identifikovat autorizované buňky
- Řízení přístupu je vynucováno AMF během registrace pomocí předplatitelských dat z UDM
- Podporuje asociaci s jedním nebo více síťovými řezy pro kombinované řízení přístupu a izolaci služeb
- Umožňuje, aby bylo UE členem více CAG, což poskytuje flexibilitu přístupu
- Zabraňuje neoprávněným předáním spojení (handover) do CAG buněk, čímž udržuje integritu uzavřené skupiny

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TR 28.828** (Rel-18) — Charging Aspects for Non-Public Networks
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.422** (Rel-20) — Telecom Management: Trace Control & Configuration
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem
- **TS 33.745** (Rel-19) — Security Study for 5G NR Femto
- **TS 33.819** (Rel-16) — 5GS Security for Vertical & LAN Services
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [CAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/cag/)
