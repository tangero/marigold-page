---
slug: "sns"
url: "/mobilnisite/slovnik/sns/"
type: "slovnik"
title: "SNS – Social Network Services"
date: 2025-01-01
abbr: "SNS"
fullName: "Social Network Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sns/"
summary: "SNS označuje kategorii telekomunikačních služeb, které uživatelům umožňují interagovat, sdílet obsah a budovat komunity prostřednictvím online platforem přístupných přes mobilní sítě. V kontextu 3GPP"
---

SNS (Sociální síťové služby) je kategorie telekomunikačních služeb pro online platformy umožňující interakci uživatelů a budování komunit, přičemž 3GPP definuje jejich architektonickou integraci s mobilními sítěmi z hlediska využití dat a kvality služby.

## Popis

Sociální síťové služby (SNS) v kontextu 3GPP nejsou jediným protokolem nebo rozhraním, ale širokou kategorií over-the-top ([OTT](/mobilnisite/slovnik/ott/)) aplikací a služeb, které využívají možnosti mobilních sítí. Standardy 3GPP se zabývají SNS definováním požadavků, architektur a prostředků, které umožňují efektivní integraci těchto služeb s mobilními sítěmi. To zahrnuje aspekty jako objevování služeb, rozlišování kvality služby (QoS), řízení politik, účtování a zabezpečené vystavení síťových [API](/mobilnisite/slovnik/api/). Architektonicky se aplikace SNS typicky nacházejí v internetové nebo doméně poskytovatele služeb, ale s 3GPP sítí komunikují prostřednictvím definovaných rozhraní, jako je [SCEF](/mobilnisite/slovnik/scef/) (Service Capability Exposure Function) v jádru 4G/5G sítě. Síť poskytuje prostředky jako ověřování uživatelů (prostřednictvím [HSS](/mobilnisite/slovnik/hss/)), lokalizační služby (prostřednictvím [GMLC](/mobilnisite/slovnik/gmlc/)) a služby oznámení.

Fungování SNS z perspektivy 3GPP sítě zahrnuje několik vrstev. Na servisní vrstvě poskytovatelé SNS nabízejí aplikace, k nimž uživatelé přistupují prostřednictvím UE (User Equipment). Úlohou 3GPP sítě je poskytovat spolehlivé, zabezpečené a kvalitně zaručené připojení. Pro pokročilejší integraci definuje 3GPP mechanismy jako konfigurace [APN](/mobilnisite/slovnik/apn/) (Access Point Name) optimalizované pro provoz SNS, které mohou směrovat data přes specifické brány ([PGW](/mobilnisite/slovnik/pgw/)/[UPF](/mobilnisite/slovnik/upf/)) s přizpůsobenými politikami. Architektura řízení politik a účtování (PCC) může pro provoz SNS aplikovat specifické QoS politiky, zajišťující lepší uživatelský zážitek pro funkce v reálném čase, jako jsou videohovory. Dále síťová API vystavená prostřednictvím SCEF/NEF (Network Exposure Function) umožňují poskytovatelům SNS žádat o síťové informace (např. stav uživatele, lokalizaci se souhlasem) nebo aktivovat síťové akce (např. odeslání SMS oznámení), což umožňuje bohatší, kontextově-aware služby.

Klíčové komponenty zapojené do podpory SNS zahrnují uživatelské zařízení (UE), rádiovou přístupovou síť (RAN), jádro sítě (s PCF, SMF, UPF) a externí aplikační server SNS. Interakce je řízena specifikacemi 3GPP, které zajišťují zabezpečení, soukromí a interoperabilitu. Například TS 22.801 popisuje servisní požadavky, TS 26.253 může pokrývat aspekty médií pro sociální TV a TS 48.016 může souviset s interworkingem se staršími GSM systémy pro přístup SNS. Síť spravuje datové přenašeče, aplikuje záznamy o účtování (CDR) za využití SNS a zajišťuje, aby masivní, často bursty provoz ze SNS negativně neovlivňoval ostatní síťové služby prostřednictvím inteligentního řízení provozu.

## K čemu slouží

Formální zohlednění sociálních síťových služeb (SNS) ve standardech 3GPP bylo motivováno explozivním růstem platforem jako Facebook, Twitter a později Instagram a jejich hlubokým dopadem na vzorce využívání mobilních sítí. Předtím byly mobilní sítě navrženy primárně pro hlas, SMS a základní prohlížení webu. Vzestup SNS vytvořil nové výzvy: masivní nárůst datového provozu, poptávku po trvalém připojení a potřebu nízké latence pro funkce jako zasílání zpráv a živé video. 3GPP začalo řešit SNS, aby zajistilo, že mobilní sítě dokážou tyto služby efektivně podporovat, neboť se staly primárním hybatelem spotřeby mobilních dat a klíčovým faktorem při volbě operátora uživatelem.

Historicky SNS začínaly jako OTT služby, fungující nezávisle na sítích operátorů. To vedlo k problémům, jako je zahlcení sítě, neschopnost garantovat kvalitu pro funkce sociálních sítí v reálném čase a promarněné příležitosti pro operátory monetizovat nebo se s těmito službami integrovat. Práce 3GPP na SNS, významně započatá v Release 8, měla za cíl vytvořit rámec pro spolupráci. Snažila se vyřešit problém, kdy byla síť pouze 'hloupou trubkou', definováním standardizovaných způsobů, jak operátoři mohou vystavovat síťové schopnosti (jako kvalita na požádání, autentizace, účtování) poskytovatelům SNS. To by umožnilo nové obchodní modely, jako je sponzorovaný datový provoz nebo vylepšená QoS pro specifické SNS aplikace, což by bylo přínosné pro operátory i poskytovatele služeb.

Vytváření požadavků a architektonických prostředků pro SNS bylo hnací silou potřeby udržovat vysokou kvalitu uživatelského zážitku (QoE), efektivně spravovat síťové zdroje a podporovat ekosystém, kde mohou inovativní služby na mobilních sítích prosperovat. Představovalo to posun v záběru 3GPP od definování pouze síťové infrastruktury k zohlednění také populárních aplikací, které na ní běží, a zajištění, že se síťová architektura vyvíjí tak, aby byla aplikacím-aware a službám přátelská.

## Klíčové vlastnosti

- Kategorie OTT aplikací využívajících mobilní konektivitu
- Generuje požadavky na vysokou datovou propustnost a nízkou latenci v sítích
- Integrována s 3GPP PCC pro rozlišování QoS a účtování
- Využívá funkce vystavení sítě (SCEF/NEF) pro přístup ke schopnostem
- Ovlivňuje architektury řízení provozu a řízení politik
- Předmět specifikací pokrývajících servisní požadavky a zpracování médií

## Definující specifikace

- **TS 22.801** (Rel-12) — Study on Non-MTC Mobile Data Application Impacts
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [SNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sns/)
