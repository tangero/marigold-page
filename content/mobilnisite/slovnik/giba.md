---
slug: "giba"
url: "/mobilnisite/slovnik/giba/"
type: "slovnik"
title: "GIBA – GPRS-IMS-Bundled Authentication"
date: 2025-01-01
abbr: "GIBA"
fullName: "GPRS-IMS-Bundled Authentication"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/giba/"
summary: "GIBA je bezpečnostní mechanismus 3GPP, který znovu využívá ověření provedené pro přístup k paketové síti GPRS/UMTS k následné autentizaci uživatele vůči IMS (IP Multimedia Subsystem). Tím odpadá potře"
---

GIBA je bezpečnostní mechanismus 3GPP, který znovu využívá ověření přístupu k paketové síti GPRS/UMTS k autentizaci uživatele vůči IMS, čímž odstraňuje potřebu samostatného IMS postupu.

## Popis

GPRS-IMS-Bundled Authentication (GIBA) je bezpečnostní architektura definovaná 3GPP, která umožňuje plynulý a efektivní tok autentizace mezi paketovou doménou ([GPRS](/mobilnisite/slovnik/gprs/)/UMTS) a IP Multimedia Subsystem (IMS). Základním principem GIBA je odvození přihlašovacích údajů pro IMS z úspěšného autentizačního a dohodovacího postupu klíčů, který byl již proveden pro podkladovou přístupovou síť GPRS/UMTS. Když se uživatelské zařízení (UE) připojí k síti GPRS, podstoupí s ní autentizační a dohodovací postup klíčů (např. [AKA](/mobilnisite/slovnik/aka/) v UMTS), jehož výsledkem je sada relakových klíčů ([IK](/mobilnisite/slovnik/ik/) a [CK](/mobilnisite/slovnik/ck/)) vytvořená mezi UE a podpůrným uzlem GPRS (SGSN). GIBA využívá tento navázaný bezpečnostní kontext.

Mechanismus funguje tak, že síť, konkrétně Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) v IMS, požádá o autentizační vektory od Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Namísto provedení plného IMS AKA postupu však HSS, který se také účastnil ověření GPRS, může poskytnout autentizační data odvozená z bezpečnostního kontextu GPRS. P-CSCF a UE pak tyto odvozené parametry použijí k vzájemné autentizaci pro přístup k IMS. Tento proces zahrnuje získání autentizačního vektoru ([AV](/mobilnisite/slovnik/av/)) z HSS P-CSCF. Tento AV obsahuje parametry jako Autentizační Token ([AUTN](/mobilnisite/slovnik/autn/)), který je vypočítán pomocí relakových klíčů GPRS, a Očekávanou Odpověď (XRES). P-CSCF zašle výzvu UE v rámci žádosti o registraci IMS.

UE, které disponuje stejnými relakovými klíči GPRS, může nezávisle vypočítat očekávané autentizační parametry. Ověří AUTN k autentizaci sítě a vypočítá odpověď (RES). UE odešle tuto RES zpět P-CSCF, který ji porovná s XRES přijatou od HSS. Shoda potvrdí identitu UE a její úspěšné ověření GPRS, čímž se udělí přístup k IMS. Architektonicky GIBA spoléhá na integraci mezi HSS (nebo starším Home Location Register, HLR) a jádrem IMS. HSS musí být informován o připojení GPRS a odpovídajících klíčích, aby mohl generovat správné odvozené autentizační vektory pro IMS. To činí z HSS ústřední komponentu, která slouží jako kotvící bod pro bezpečnostní kontexty jak přístupové, tak servisní vrstvy.

Úlohou GIBA v síti je optimalizace doby nastavení služby pro IMS aplikace, jako je Voice over LTE (VoLTE), tím, že se vyhne duplicitnímu, plnému autentizačnímu cyklu. Snižuje signalizační zátěž v jádru sítě a spotřebu baterie UE spojenou s kryptografickými výpočty. Představuje klíčový bod konvergence mezi staršími sítěmi s přepojováním okruhů/paketů a plně IP jádrem IMS, což usnadňuje plynulejší přechod ke sjednoceným komunikačním službám.

## K čemu slouží

GIBA byla vytvořena, aby řešila neefektivitu a zhoršení uživatelského zážitku způsobené vyžadováním samostatných, sekvenčních autentizačních postupů, když uživatel přistupuje k IMS službám přes paketovou síť 3GPP. Před GIBA se UE nejprve ověřilo vůči síti GPRS/UMTS (např. pomocí UMTS AKA), aby získalo IP konektivitu. Poté, když se pokusilo zaregistrovat k IMS službě, jako je hlasové nebo videohovory, muselo provést druhý, nezávislý autentizační postup (IMS AKA) s jádrem IMS. Toto dvojité ověření prodlužovalo dobu navázání hovoru, spotřebovávalo další rádiové a jádrové síťové signalizační prostředky a rychleji vybíjelo baterii UE kvůli dodatečnému kryptografickému zpracování.

Historický kontext představuje zavedení IMS ve 3GPP Release 5 jako platformy pro poskytování multimediálních služeb. Zpočátku bylo IMS navrženo jako přístupově agnostické, což logicky vedlo k jeho vlastnímu autentizačnímu rámci. Pro přístupy definované 3GPP (GPRS, UMTS) to však vedlo k redundanci, protože operátor již uživatele ověřil a navázal zabezpečený kanál na přístupové vrstvě. GIBA byla standardizována, aby využila této existující důvěry a bezpečnostního kontextu. Řeší problém vytvořením bezpečnostní asociace mezi oběma vrstvami, což umožňuje IMS důvěřovat výsledku ověření podkladové sítě GPRS.

Tento přístup řešil omezení nespojitého modelu, konkrétně latenci při zahájení služby a zbytečnou zátěž autentizačního centra (AuC) a HSS. Spojením ověření umožňuje GIBA rychlejší registraci IMS, což je klíčové pro služby komunikace v reálném čase. Také zjednodušuje celkovou bezpečnostní architekturu pro operátory nasazující IMS přes jejich vlastní rádiový přístup 3GPP, čímž činí spuštění služby efektivnějším a zlepšuje vnímanou rychlost odezvy pro koncového uživatele.

## Klíčové vlastnosti

- Odstraňuje samostatný IMS AKA postup pro přístup 3GPP
- Odvozuje přihlašovací údaje pro IMS z navázaných bezpečnostních klíčů GPRS/UMTS (IK, CK)
- Snižuje signalizační režii a latenci během registrace IMS
- Využívá HSS jako společný bezpečnostní kotvící bod pro přístupovou i servisní vrstvu
- Zlepšuje uživatelský zážitěk rychlejším zpřístupněním služeb
- Snižuje spotřebu energie UE tím, že se vyhne duplicitním kryptografickým výpočtům

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.203** (Rel-19) — IMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [GIBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/giba/)
