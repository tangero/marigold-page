---
slug: "rvas"
url: "/mobilnisite/slovnik/rvas/"
type: "slovnik"
title: "RVAS – Roaming Value-Added Services"
date: 2026-01-01
abbr: "RVAS"
fullName: "Roaming Value-Added Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rvas/"
summary: "Roaming Value-Added Services (RVAS) jsou standardizované služby nabízené účastníkům při roamování mimo jejich domovskou síť. Umožňují konzistentní přístup k rozšířeným službám, jako je streamování, hr"
---

RVAS je soubor standardizovaných služeb, které poskytují roamujícím účastníkům konzistentní přístup k rozšířeným aplikacím, jako je streamování nebo hraní her, čímž zlepšují uživatelský zážitek a vytvářejí příjmy pro operátory.

## Popis

Roaming Value-Added Services (RVAS) představují rámec v rámci standardů 3GPP, zavedený ve vydání Release 19, pro definici a poskytování rozšířených služeb účastníkům během jejich roamování. Architektura zahrnuje koordinaci mezi navštívenou veřejnou pozemní mobilní sítí ([VPLMN](/mobilnisite/slovnik/vplmn/)) a domovskou veřejnou pozemní mobilní sítí ([HPLMN](/mobilnisite/slovnik/hplmn/)) za účelem zajištění kontinuity služeb a jejich kvality. Klíčové komponenty zahrnují Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro správu profilů účastníků, Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro dynamické vynucování politik a Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) nebo Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) pro bezpečné zpřístupnění služeb poskytovatelům aplikací třetích stran. Rámec využívá stávající roamingová rozhraní a protokoly, jako jsou ty definované v Diameter-based S6a/S6d nebo HTTP-based Nudm/Npcf rozhraních, pro výměnu autorizačních, politických a účtovacích informací služeb.

Operačně, když účastník přejde do roamingu v navštívené síti, HPLMN poskytne VPLMN profil RVAS účastníka, který detailně popisuje přihlášené přidané služby a související politiky. VPLMN pak tyto politiky aplikuje, aby umožnila nebo upřednostnila konkrétní služby, a zajistila tak, že účastník získá stejný servisní zážitek jako ve své domovské síti. Tento proces zahrnuje dynamické řízení politik, kde PCF v domovské nebo navštívené síti může upravit parametry Quality of Service (QoS), jako je přidělení šířky pásma a cíle latence, na základě aktuálních podmínek sítě a požadavků služby. Účtování a fakturace jsou řešeny prostřednictvím integrovaných online a offline účtovacích systémů ([OCS](/mobilnisite/slovnik/ocs/)/OFCS), přičemž jsou generovány podrobné záznamy pro vypořádání mezi operátory.

Úloha RVAS v síti spočívá v překlenutí mezery mezi základní konektivitou a poskytováním prémiových služeb v roamingových scénářích. Řeší technické výzvy udržování smluv o úrovni služeb (SLA) napříč administrativními hranicemi a umožňuje funkce jako garantované přenosové rychlosti pro video streamování, přístup s nízkou latencí pro cloudové hraní her a spolehlivou konektivitu pro kritické IoT aplikace. Standardizací těchto schopností 3GPP zajišťuje interoperabilitu mezi sítěmi různých operátorů, podporuje globální ekosystém, kde mohou být pokročilé služby bezproblémově nabízeny roamujícím uživatelům, čímž se zvyšuje spokojenost zákazníků a podporuje adopce služeb 5G a novějších generací.

## K čemu slouží

RVAS byly vytvořeny za účelem řešení rostoucí poptávky po kvalitních přidaných službách, zatímco uživatelé roamují, což je scénář, kde byl servisní zážitek historicky nekonzistentní nebo omezený. Před jejich standardizací se operátoři často spoléhali na bilaterální dohody a proprietární řešení pro nabídku rozšířených roamingových služeb, což vedlo k fragmentaci, zvýšené složitosti a omezené škálovatelnosti. Tento přístup bránil široké dostupnosti služeb, jako je streamování videa ve vysokém rozlišení, hraní her v reálném čase a podniková IoT řešení pro roamující účastníky, protože technická a komerční interoperabilita byla náročná.

Motivace pro RVAS vychází z vývoje mobilních sítí směrem k 5G a rostoucího významu diferenciace služeb. S rozšířením datově náročných aplikací se operátoři snažili monetizovat roaming nad rámec základního hlasového a datového přístupu nabídkou služeb v různých úrovních. RVAS poskytují standardizovaný rámec pro definici, autorizaci a poskytování těchto služeb, což zajišťuje, že účastníci obdrží konzistentní zážitek bez ohledu na svou polohu. Řeší problémy související s vynucováním politik napříč síťovými hranicemi, dynamickým řízením QoS a integrovaným účtováním, což umožňuje operátorům efektivně uvádět nové příjmové služby.

Historicky se roaming zaměřoval primárně na základní konektivitu, přičemž přidané služby byly druhořadé. RVAS představují změnu paradigmatu tím, že schopnosti služeb integrují do roamingové architektury od samého počátku. Řeší omezení předchozích přístupů, jako je nedostatek detailní kontroly politik a neschopnost zpřístupnit síťové schopnosti poskytovatelům služeb třetích stran v kontextu roamingu. Tímto způsobem RVAS usnadňují inovace, umožňují operátorům a poskytovatelům aplikací spolupracovat na poskytování přizpůsobených zážitků roamujícím uživatelům, čímž zvyšují celkovou hodnotovou nabídku mobilních služeb.

## Klíčové vlastnosti

- Standardizovaná autorizace služeb a výměna profilů mezi domovskou a navštívenou sítí
- Dynamické řízení politik pro vynucování Quality of Service (QoS) během roamingu
- Integrované účtovací mechanismy pro přidané služby s podporou vypořádání
- Zpřístupnění síťových schopností poskytovatelům aplikací třetích stran prostřednictvím SCEF/NEF
- Podpora různých typů služeb včetně streamování, hraní her a IoT aplikací
- Zajišťuje kontinuitu služeb a konzistentní uživatelský zážitek napříč síťovými hranicemi

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.877** (Rel-19) — Study on Roaming Value-Added Services

---

📖 **Anglický originál a plná specifikace:** [RVAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rvas/)
