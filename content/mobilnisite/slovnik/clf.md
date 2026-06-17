---
slug: "clf"
url: "/mobilnisite/slovnik/clf/"
type: "slovnik"
title: "CLF – Connectivity session Location and repository Function"
date: 2025-01-01
abbr: "CLF"
fullName: "Connectivity session Location and repository Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/clf/"
summary: "CLF je síťová funkce v IP Multimedia Subsystem (IMS), která ukládá a poskytuje informace o poloze uživatelského zařízení během spojovacích relací. Umožňuje efektivní směrování relací a doručování služ"
---

CLF je síťová funkce v síti IMS, která ukládá a poskytuje informace o poloze uživatelského zařízení během spojovacích relací, aby umožnila efektivní směrování a doručování služeb.

## Popis

Connectivity session Location and repository Function (CLF) je klíčová komponenta v architektuře 3GPP IP Multimedia Subsystem (IMS), speciálně navržená pro správu a poskytování informací o poloze uživatelského zařízení během aktivních spojovacích relací. Funguje jako centralizovaná databáze, která udržuje aktuální data o síťových připojovacích bodech a stavu připojení uživatelů IMS napříč různými přístupovými sítěmi, včetně 3GPP i ne-3GPP přístupových technologií. CLF komunikuje s více síťovými elementy, aby tyto informace o poloze shromažďovala a distribuovala, což umožňuje efektivní směrování relací a doručování služeb.

Z architektonického hlediska funguje CLF jako samostatný síťový element, který interaguje s několika klíčovými komponentami IMS. Udržuje rozhraní s Interrogating Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) a Serving Call Session Control Function (S-CSCF), aby poskytovala informace o poloze během navazování relace a rozhodování o směrování. CLF také komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) za účelem získání informací o profilu účastníka a s různými elementy přístupové sítě za účelem shromažďování aktualizací o stavu připojení. Tento síťově-centrický přístup umožňuje CLF udržovat komplexní přehled o připojení uživatele napříč heterogenními sítěmi.

CLF funguje prostřednictvím kombinace registračních, dotazovacích a notifikačních mechanismů. Když uživatelské zařízení naváže připojení prostřednictvím jakékoli přístupové sítě, příslušné síťové elementy o tom notifikují CLF a poskytnou informace o aktuální poloze a stavu připojení uživatele. CLF tyto informace ukládá ve své databázi a asociuje je s veřejnou identitou uživatele. Během navazování relace, když přijde příchozí požadavek na relaci, [I-CSCF](/mobilnisite/slovnik/icscf/) se dotazuje CLF, aby zjistil aktuální stav připojení a polohu uživatele. Na základě těchto informací CLF poskytne instrukce pro směrování, které nasměrují relaci na příslušný S-CSCF obsluhující uživatele v daném místě.

Klíčové komponenty CLF zahrnují databázi úložiště polohy, která uchovává aktuální informace o připojení; zpracovatel dotazů, který obsluhuje dotazy na polohu od síťových elementů; a notifikační rozhraní, které přijímá aktualizace od přístupových sítí o změnách v připojení uživatele. CLF také zahrnuje schopnosti správy předplatného, které umožňují síťovým elementům přihlásit se k odběru notifikací o změně polohy pro konkrétní uživatele. Tento proaktivní notifikační mechanismus umožňuje efektivní směrování relací bez nutnosti opakovaných dotazů, čímž snižuje signalizační zátěž a zlepšuje doby navazování relace.

CLF hraje klíčovou roli při umožnění plynulé mobility a kontinuity služeb napříč různými přístupovými sítěmi. Udržováním přesných informací o poloze podporuje funkce jako výběr přístupové sítě, kontinuitu relace během předávání a efektivní směrování multimediálních relací. Schopnost CLF pracovat s 3GPP i ne-3GPP přístupovými technologiemi ji činí nezbytnou pro konvergované sítě, kde uživatelé mohou přepínat mezi různými typy připojení při zachování svých IMS služeb.

## K čemu slouží

CLF byla zavedena ve 3GPP Release 7, aby řešila rostoucí složitost směrování relací v konvergovaných sítích IP Multimedia Subsystem (IMS). Když operátoři začali nasazovat IMS služby napříč více přístupovými technologiemi, včetně 3GPP mobilních sítí i ne-3GPP přístupů jako WiFi, objevila se potřeba centralizovaného mechanismu pro sledování polohy připojení uživatelů. Předchozí přístupy spoléhaly na distribuované informace o poloze uložené v různých síťových prvcích, což vedlo k neefektivnímu směrování relací, zvýšené signalizační zátěži a obtížím při udržování kontinuity služeb během událostí mobility.

Před zavedením CLF čelily IMS sítě výzvám v efektivním směrování relací k uživatelům, kteří mohli být připojeni přes více přístupových bodů současně nebo kteří často měnili své připojovací body. Tradiční přístup dotazování více síťových elementů na informace o poloze vedl ke zvýšeným zpožděním při navazování relací a vyšší signalizační zátěži v síti. CLF tyto problémy vyřešila tím, že poskytla jediný autoritativní zdroj informací o připojení uživatele, což umožnilo rychlejší rozhodování o směrování relací a snížení celkové signalizace v síti.

Vytvoření CLF bylo motivováno potřebou podporovat konvergované služby napříč heterogenními sítěmi při zachování efektivního provozu sítě. Když operátoři rozšiřovali své služby o fixně-mobilní konvergenci a připojení přes více přístupů, schopnost přesně sledovat a využívat informace o poloze uživatele se stala klíčovou pro doručování služeb. CLF umožnila operátorům optimalizovat své síťové zdroje prostřednictvím inteligentního směrování založeného na aktuálním stavu připojení, a zároveň podporovat regulatorní požadavky na služby založené na poloze a směrování nouzových volání.

## Klíčové vlastnosti

- Centralizovaná databáze pro informace o poloze připojení uživatele
- Aktuální sledování uživatelského zařízení napříč více přístupovými sítěmi
- Rozhraní s I-CSCF pro efektivní rozhodování o směrování relací
- Podpora 3GPP i ne-3GPP přístupových technologií
- Mechanismus notifikací o změnách polohy založený na předplatném
- Integrace s HSS pro korelaci s profilem účastníka

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.203** (Rel-19) — IMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [CLF na 3GPP Explorer](https://3gpp-explorer.com/glossary/clf/)
