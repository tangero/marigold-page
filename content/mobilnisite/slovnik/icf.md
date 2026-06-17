---
slug: "icf"
url: "/mobilnisite/slovnik/icf/"
type: "slovnik"
title: "ICF – Initial Connectivity Function"
date: 2025-01-01
abbr: "ICF"
fullName: "Initial Connectivity Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/icf/"
summary: "Bezpečnostní funkce definovaná pro komunikaci typu stroj-stroj (MTC) a IoT zařízení. Působí jako důvěryhodný zprostředkovatel během počátečního připojení zařízení k síti a usnadňuje zabezpečený bootst"
---

ICF je bezpečnostní funkce pro MTC a IoT zařízení, která během počátečního připojení k síti funguje jako důvěryhodný zprostředkovatel a usnadňuje zabezpečený bootstrap proces a zřizování přihlašovacích údajů.

## Popis

Initial Connectivity Function (ICF) je síťová bezpečnostní entita specifikovaná v rámci 3GPP pro zabezpečení počátečního vstupu do sítě a bootstrap procedury omezených zařízení, zejména v kontextu komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) a internetu věcí (IoT). Jejím primárním úkolem je fungovat jako důvěryhodná třetí strana nebo bootstrap server, který pomáhá zařízení, jež může mít pouze minimální předkonfigurované přihlašovací údaje (například továrně instalovaný předem sdílený klíč (PSK) nebo certifikát), navázat zabezpečené spojení se zamýšleným poskytovatelem služeb nebo aplikačním serverem. ICF je součástí širší bezpečnostní architektury 3GPP pro MTC a často interaguje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a MTC Interworking Function ([MTC-IWF](/mobilnisite/slovnik/mtc-iwf/)).

Z architektonického hlediska může být ICF umístěna v domácí síti zařízení nebo ve vyhrazené síti služeb. Její fungování začíná ve chvíli, kdy se IoT zařízení poprvé zapne a pokusí se připojit k síti. Zařízení se k síti autentizuje pomocí svých počátečních, omezených přihlašovacích údajů (např. PSK sdíleného s ICF). Po úspěšné autentizaci ICF do procesu vstoupí. S zařízením bezpečně komunikuje, často pomocí tunelu TLS nebo [DTLS](/mobilnisite/slovnik/dtls/) navázaného s počátečními přihlašovacími údaji. Prostřednictvím tohoto zabezpečeného kanálu ICF zařízení zřídí potřebné dlouhodobé nebo služebně specifické přihlašovací údaje potřebné pro následný běžný přístup k síti a komunikaci s jeho konečným aplikačním serverem ([AS](/mobilnisite/slovnik/as/)). To může zahrnovat zřízení nových přihlašovacích údajů SIM (pro scénáře eSIM), služebně specifického klíče nebo certifikátů.

Klíčové komponenty ICF zahrnují zabezpečené úložiště pro bootstrap klíče, protokoly pro zabezpečené doručování přihlašovacích údajů (v souladu se standardy jako [IETF](/mobilnisite/slovnik/ietf/) Bootstrapping Remote Secure Key Infrastructures (BRSKI) nebo Lightweight M2M (LwM2M) bootstrap) a rozhraní k vystavovatelům přihlašovacích údajů (jako certifikační autorita) nebo k HSS. Její role je klíčová pro správu životního cyklu IoT zařízení, protože umožňuje 'zero-touch' zřizování ve velkém měřítku. Odděluje výrobní a expediční proces (kde je nainstalován obecný bootstrap přihlašovací údaj) od procesu nasazení (kde jsou přiřazeny provozně specifické přihlašovací údaje zařízení), čímž zvyšuje bezpečnost a provozní flexibilitu. Specifikace jako TS 33.127 a TS 33.128 podrobně popisují bezpečnostní procedury a architekturu zahrnující ICF.

## K čemu slouží

ICF byla vytvořena, aby řešila významné bezpečnostní a provozní výzvy spojené s nasazením obrovského množství IoT zařízení. Tradiční zřizování mobilních zařízení, soustředěné kolem univerzální integrované obvodové karty (UICC), předpokládá řiditelný životní cyklus. V IoT mohou být zařízení nasazena na nepřístupných místech, mít extrémně dlouhou životnost nebo být vyrobena jednou entitou a provozována jinou. Předzásobení každého zařízení jeho konečnými provozními přihlašovacími údaji již ve výrobě je nepružné a riskantní. ICF to řeší tím, že umožňuje zabezpečený proces vzdáleného bootstrapu.

Historický kontext vychází z práce 3GPP na bezpečnosti [MTC](/mobilnisite/slovnik/mtc/) počínaje Release 9 a vyvíjející se v pozdějších releasech. Rané studie MTC identifikovaly potřebu vylepšených bezpečnostních opatření pro zařízení, která nemusí mít UICC nebo mohou používat odlehčené autentizační metody. Omezení předchozích přístupů spočívalo v absenci standardizovaného, síťově asistovaného mechanismu pro přechod zařízení od jednoduchých, továrních výchozích přihlašovacích údajů k robustní, služebně specifické sadě přihlašovacích údajů plně automatizovaným a bezpečným způsobem. ICF tento mechanismus poskytuje.

K jejímu vytvoření vedla potřeba škálovatelného a bezpečného onboardingu. Umožňuje výrobcům zařízení instalovat jediný typ bootstrap přihlašovacích údajů (např. PSK) na všechna zařízení, což zjednodušuje dodavatelský řetězec. Síťoví operátoři nebo poskytovatelé služeb mohou následně, a to vzdáleně, prostřednictvím důvěryhodné ICF zřídit jedinečné přihlašovací údaje potřebné pro jejich konkrétní službu. To řeší problémy správy přihlašovacích údajů, snižuje riziko jejich kompromitace ve výrobě a podporuje obchodní modely jako je přeprodej zařízení nebo převod služby. Je to základní prvek pro zabezpečená hromadná nasazení IoT, jak jsou koncipována v releasech zaměřených na CIoT a LTE-M/NB-IoT.

## Klíčové vlastnosti

- Funguje jako důvěryhodný bootstrap server pro počáteční připojení IoT/MTC zařízení
- Podporuje autentizaci pomocí počátečních předem sdílených klíčů (PSK) nebo certifikátů
- Navazuje zabezpečený kanál pro následné zřizování přihlašovacích údajů
- Umožňuje vzdálené zřizování provozních klíčů, certifikátů nebo eSIM profilů
- Integruje se s 3GPP síťovými elementy, jako je HSS, pro správu přihlašovacích údajů
- Umožňuje zero-touch, škálovatelné nasazení omezených zařízení

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MTC-IWF – Machine Type Communications - InterWorking Function](/mobilnisite/slovnik/mtc-iwf/)

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security

---

📖 **Anglický originál a plná specifikace:** [ICF na 3GPP Explorer](https://3gpp-explorer.com/glossary/icf/)
