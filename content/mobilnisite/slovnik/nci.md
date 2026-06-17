---
slug: "nci"
url: "/mobilnisite/slovnik/nci/"
type: "slovnik"
title: "NCI – Native Code Identifier"
date: 2025-01-01
abbr: "NCI"
fullName: "Native Code Identifier"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nci/"
summary: "Identifikátor používaný ve specifikacích 3GPP k jednoznačné referenci konkrétní části nativního kódu nebo softwarové komponenty uvnitř síťového uzlu. Pomáhá při správě softwaru, správě verzí a hlášení"
---

NCI (Native Code Identifier) je jedinečný identifikátor pro konkrétní část nativního kódu nebo softwarové komponenty uvnitř síťového uzlu, používaný pro správu softwaru, správu verzí a hlášení poruch v systémech 3GPP.

## Popis

Native Code Identifier (NCI) je koncept definovaný ve specifikacích 3GPP, primárně v oblasti správy a provozu (např. TS 32.260). Slouží jako jedinečná značka pro diskrétní modul nebo komponentu nativního softwarového kódu běžícího uvnitř síťového elementu. Na rozdíl od identifikátorů pro fyzické zdroje, jako jsou buňky nebo účastníci, se NCI vztahuje k softwarové architektuře síťových uzlů, jako jsou základnové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), funkce jádra sítě ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)) nebo systémy správy.

Pokud jde o způsob fungování, NCI je typicky přidělen výrobcem zařízení nebo vývojářem softwaru během procesu sestavení a integrace. Je vestavěn do samotné softwarové komponenty a může být zpřístupněn systémům správy, provozu a údržby (OAM) sítě prostřednictvím rozhraní pro správu. Když síťový element hlásí svůj stav, výkonnostní metriky nebo poruchové alarmy, může zahrnout NCI příslušného softwarového modulu. To umožňuje operátorům sítě přesně určit nejen to, že došlo k poruše, ale i to, která konkrétní softwarová komponenta poruchu vygenerovala nebo má problémy.

Architektura zahrnuje spravovaný síťový element ([NE](/mobilnisite/slovnik/ne/)) a řídicí systém (OAM systém). NE obsahuje různé softwarové procesy, knihovny nebo moduly firmwaru, z nichž každý může být asociován s NCI. Tyto identifikátory jsou strukturovány tak, aby byly jedinečné v rámci daného NE nebo případně v rámci softwarové sady dodavatele. Jsou komunikovány prostřednictvím standardizovaných protokolů pro správu, jako je SNMP, nebo na základě informačních modelů definovaných 3GPP v rozhraních, jako je Itf-N. OAM systém používá tyto NCI ke korelaci událostí, sledování verzí softwaru napříč nasazeními a správě softwarových aktualizací nebo záplat cílených na konkrétní komponenty.

Jeho role v síti spočívá v podpoře robustní správy životního cyklu softwaru. Ve velkých, distribuovaných telekomunikačních sítích provozujících komplexní software od více dodavatelů je klíčové pro řešení problémů a údržbu identifikovat, který přesně kódový modul je zodpovědný za určité chování. NCI poskytuje tuto granularitu. Také usnadňuje správu verzí softwaru a kontrolu kompatibility. Při upgradu síťového elementu může OAM systém ověřit NCI a přidružené verze všech komponent, aby zajistil konzistenci a předešel konfliktům. Dále ve scénářích virtualizovaných síťových funkcí (VNF), kde je software oddělen od hardwaru, se identifikátory jako NCI stávají ještě důležitějšími pro sledování instancí komponent napříč cloudovými infrastrukturami.

## K čemu slouží

NCI byl vytvořen, aby řešil rostoucí složitost softwaru v telekomunikačních síťových zařízeních. Jak se sítě vyvíjely z relativně monolitických systémů orientovaných na hardware ve 2G/3G k softwarově definovaným a virtualizovaným systémům ve 4G a 5G, zvýšila se potřeba jemně granulované správy softwaru. Operátoři potřebovali nástroje k identifikaci, správě verzí a správě jednotlivých softwarových komponent uvnitř uzlu pro efektivní provoz, údržbu a řešení problémů.

Problém, který řeší, je nejednoznačnost v hlášení poruch a softwarových aktualizacích. Bez jedinečného identifikátoru pro kódové moduly může poruchový alarm pouze naznačovat vysokou úroveň selhání v síťovém elementu, což nutí inženýry ručně diagnostikovat, který softwarový proces spadl nebo se choval nesprávně. To zpomaluje řešení. Podobně při aplikaci softwarové záplaty, bez identifikátorů na úrovni komponent, může být aktualizace aplikována na celý obraz uzlu, což může potenciálně ovlivnit nesouvisející stabilní komponenty. NCI umožňuje cílenou správu.

Jeho motivace vychází z posunu odvětví k více softwarově řízeným sítím a souvisejících požadavků na automatizaci v OAM. Standardy jako 3GPP TS 32.260 (Fault Management) a TS 32.274 (Performance Management) detailně popisují informační modely potřebné pro rozhraní správy. Zařazení NCI poskytuje standardizované pole pro dodavatele k hlášení softwarově specifických informací, což umožňuje interoperabilitu systémů správy od více dodavatelů. Pomáhá operátorům spravovat hybridní sítě obsahující zařízení od různých dodavatelů, z nichž každý má svou vlastní interní softwarovou architekturu, tím, že poskytuje společný referenční bod pro softwarové komponenty.

## Klíčové vlastnosti

- Jedinečný identifikátor pro modul nativního softwarového kódu uvnitř síťového elementu
- Používá se primárně v kontextech správy, provozu a údržby (OAM)
- Zpřístupněno prostřednictvím rozhraní pro správu (např. Itf-N) pro hlášení poruch a výkonnosti
- Umožňuje jemně granulovanou správu verzí softwaru a cílenou správu záplat
- Podporuje řešení problémů propojením alarmů s konkrétními softwarovými komponentami
- Aplikovatelné jak na fyzické síťové uzly, tak na virtualizované síťové funkce (VNF)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [NCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nci/)
