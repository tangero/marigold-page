---
slug: "mvigc"
url: "/mobilnisite/slovnik/mvigc/"
type: "slovnik"
title: "MVIGC – MCVideo Imminent peril Group Call"
date: 2025-01-01
abbr: "MVIGC"
fullName: "MCVideo Imminent peril Group Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvigc/"
summary: "Vysoce prioritní, přednostní skupinová hovorová služba zřízená pro skupinu MCVideo Imminent Peril Group (MVIG) během mimořádné události. Poskytuje okamžitou videokomunikaci pro koordinovaný zásah před"
---

MVIGC je vysoce prioritní, přednostní skupinová hovorová služba MCVideo pro předdefinovanou skupinu záchranných složek, která poskytuje okamžitou videokomunikaci během mimořádné události.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Imminent Peril Group Call (MVIGC) je skutečná komunikační relace vytvořená pro [MVIG](/mobilnisite/slovnik/mvig/) při vyhlášení stavu bezprostředního ohrožení. Jedná se o specifický typ Mission Critical Group Call, který využívá služební prostředky MCVideo k založení skupinové komunikační relace v reálném čase s videem jako primárním médiem. Hovor je charakteristický svou vysokou prioritou a schopností přednostně vytěsnit jiný síťový provoz. Proces začíná, když autorizovaný uživatel nebo systém (např. dispečerská aplikace) zahájí požadavek na MVIGC s odkazem na konkrétní identifikátor MVIG. Tento požadavek je odeslán aplikačnímu serveru MCVideo, který jej autentizuje a načte konfiguraci MVIG.

Z architektonického hlediska následně MCVideo [AS](/mobilnisite/slovnik/as/) interaguje s podkladovou sítí 3GPP – zpočátku s Evolved Packet Core (EPC) v LTE nebo s 5G Core Network (5GC) – aby zřídil potřebné přenosové prostředky pro skupinový hovor. To zahrnuje signalizaci směrem k Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro aplikaci vyhrazené QoS politiky pro MVIGC, která zajišťuje garantovaný datový tok, prioritu a potenciálně přednostní schopnosti. Síť zřizuje individuální přenosové cesty nebo QoS toky pro každého člena MVIG a spojuje je se společnou funkcí multimediálních prostředků, která míchá a distribuuje video a audio streamy. Mezi klíčové zapojené komponenty patří MCVideo AS, Group Communication System Application Server (GCS AS), Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) a entity pro správu politik a relací v jádru sítě.

Jeho úlohou je poskytnout okamžitou, spolehlivou a kvalitní videokonferenci pro záchranné složky. Nastavení hovoru je optimalizováno pro rychlost, často obchází běžné postupy vyzvánění, aby automaticky připojilo všechny členy. Během hovoru mechanismy řízení práva k vysílání (floor control) spravují, kdo může mluvit nebo sdílet video, a relace přetrvává, dokud není explicitně ukončena. MVIGC využívá definici skupiny k zajištění, že jsou zahrnuti všichni potřební personál, a že síť zachází s touto komunikací jako s nejkritičtějším provozem, což je nezbytné pro udržení povědomí o situaci a koordinaci velení během rychle se vyvíjející krize.

## K čemu slouží

MVIGC byl standardizován, aby splnil požadavek na okamžitý, video založený skupinový komunikační kanál, který se aktivuje automaticky po vyhlášení mimořádné události. Tradiční telekonferenční řešení nebo push-to-talk over cellular (PoC) řešení postrádala garantovanou prioritu, přednostní právo a rychlé mechanismy nastavení potřebné pro situace života a smrti. Záchranné složky potřebovaly systém, kde jediné upozornění spustí plnohodnotnou videokonferenci se všemi relevantními stranami bez jakéhokoli ručního vytáčení nebo zpoždění spojení.

MVIGC řeší kritickou mezeru mezi identifikací skupiny v bezprostředním ohrožení ([MVIG](/mobilnisite/slovnik/mvig/)) a skutečným zřízením funkčního komunikačního kanálu pro tuto skupinu. Uvádí tak koncept MVIG do provozní praxe. Motivace vycházela z potřeby bezpečnostních složek využívat širokopásmové video pro lepší povědomí o situaci – vidět místo katastrofy, podezřelého nebo dispozice budovy – při zachování funkce okamžitého skupinového spojení z jejich starých rádiových systémů. Definováním MVIGC jako standardizované služby zajistil 3GPP, že aplikace a sítě pro misně kritické služby od různých dodavatelů mohou spolupracovat na poskytnutí této životně důležité funkce, což umožňuje efektivní zásah více složek během velkých incidentů.

## Klíčové vlastnosti

- Automatické nebo na požadání zřízení skupinového hovoru pro předdefinovanou MVIG
- Vysoce prioritní nastavení relace s možností přednostního přidělení prostředků na úkor jiného provozu
- Integrované sdílení videa, audia a dat v rámci skupinového hovoru
- Aplikace QoS profilů pro misně kritické služby (např. GBR, vysoká úroveň priority)
- Podpora řízení práva k vysílání (floor control) a identifikace mluvčího
- Bezproblémová integrace s architekturou služby MCVideo a podkladovou jádrovou sítí 3GPP

## Související pojmy

- [MVIG – MCVideo Imminent peril Group](/mobilnisite/slovnik/mvig/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVIGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvigc/)
