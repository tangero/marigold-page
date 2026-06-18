---
slug: "hpsim"
url: "/mobilnisite/slovnik/hpsim/"
type: "slovnik"
title: "HPSIM – Hosting Party Subscription Identity Module"
date: 2025-01-01
abbr: "HPSIM"
fullName: "Hosting Party Subscription Identity Module"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hpsim/"
summary: "Hosting Party Subscription Identity Module je logická entita definovaná pro komunikaci typu stroj-stroj (M2M). Představuje předplatné hostující strany, což je subjekt, který poskytuje konektivitu nebo"
---

HPSIM je logická entita typu stroj-stroj (M2M) představující předplatné poskytovatele služeb, která umožňuje oddělené účtování a správu od koncového uživatelského zařízení.

## Popis

Hosting Party Subscription Identity Module (HPSIM) je koncept správy předplatného a identity specifikovaný v 3GPP TS 31.111 pro architekturu komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) nebo internetu věcí (IoT). Architektonicky se jedná o logický modul nebo profil asociovaný nikoli s koncovým M2M zařízením uživatele, ale s 'hostující stranou' – subjektem, jako je poskytovatel M2M služeb, podnik nebo systémový integrátor, který spravuje a poskytuje služby pro flotilu M2M zařízení. Funguje tak, že poskytuje samostatnou identitu předplatného (potenciálně propojenou s rozsahem [IMSI](/mobilnisite/slovnik/imsi/) nebo specifickou sadou přihlašovacích údajů), která se používá pro síťovou autentizaci, autorizaci a účtování za službu konektivity spotřebovávanou zařízeními pod jeho správou.

Klíčové komponenty zahrnují přihlašovací údaje HPSIM uložené zabezpečeně (konceptuálně v UICC nebo integrovaném [SIM](/mobilnisite/slovnik/sim/)), M2M zařízení, infrastrukturu poskytovatele M2M služeb a jádrovou síť mobilního operátora ([MNO](/mobilnisite/slovnik/mno/)). HPSIM umožňuje dvouúrovňový model identity: M2M zařízení může mít svou vlastní identitu předplatného (např. v SIM zařízení), zatímco síťová konektivita je autorizována a účtována na základě předplatného hostující strany (HPSIM). To umožňuje hostující straně vystupovat jako přeprodejce nebo správce konektivity. Jejím úkolem je oddělit vztah poskytování služeb a účtování od individuálního předplatného zařízení, čímž se zjednodušují rozsáhlá nasazení IoT, kde je jediný subjekt zodpovědný za tisíce zařízení.

HPSIM usnadňuje funkce jako vzdálená provize a správa předplatných zařízení hostující stranou. Interaguje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) operátora nebo ekvivalentní entitou za účelem autentizace práva hostující strany povolit konektivitu pro svá přidružená zařízení. Tento model podporuje obchodní scénáře, kdy jsou náklady na konektivitu zahrnuty do poplatku za službu placeného hostující straně, spíše než aby je přímo spravoval vlastník zařízení, což zefektivňuje operace pro vertikální IoT aplikace.

## K čemu slouží

HPSIM byl vytvořen pro řešení specifických obchodních a provozních modelů rozsáhlých nasazení komunikace stroj-stroj a IoT. Tradiční mobilní předplatná byla navržena pro lidské uživatele s vztahem jedna ku jedné mezi [SIM](/mobilnisite/slovnik/sim/) kartou, zařízením a fakturačním účtem. Tento model se stává těžkopádným a neefektivním pro podniky nasazující tisíce senzorů nebo zařízení, které vyžadují individuální správu a fakturaci pro každé SIM zařízení.

Jeho zavedení ve verzi 11 (Release 11) bylo motivováno potřebou podpory 'poskytovatelů M2M služeb' jakožto odlišné role v ekosystému. HPSIM umožňuje oddělení zájmů: výrobce nebo vlastník zařízení spravuje aplikaci zařízení, zatímco hostující strana (poskytovatel služeb) spravuje předplatné síťové konektivity. Tím se řeší problémy škálovatelné správy předplatných, agregované fakturace a flexibilní provize služeb. Umožňuje poskytovatelům služeb nakupovat konektivitu hromadně od [MNO](/mobilnisite/slovnik/mno/) a nabízet svým podnikovým zákazníkům šité datové plány na míru, což podporuje růst trhu M2M snižováním složitosti a umožňováním nových obchodních vztahů. Řeší omezení tradičního SIM modelu zavedením hierarchické struktury předplatného přizpůsobené světu IoT.

## Klíčové vlastnosti

- Definuje identitu předplatného pro hostující stranu M2M oddělenou od identity koncového zařízení
- Umožňuje škálovatelnou správu a fakturaci pro velké flotily IoT zařízení pod jednou hostující stranou
- Podporuje obchodní modely, kde je konektivita přeprodávána nebo spravována poskytovatelem služeb
- Usnadňuje vzdálenou provizi a správu síťových přihlašovacích údajů zařízení
- Integruje se s architekturami sítí MTC/IoT pro účely autentizace a autorizace
- Odděluje poskytování služeb od individuálního předplatného zařízení

## Související pojmy

- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [HPSIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/hpsim/)
