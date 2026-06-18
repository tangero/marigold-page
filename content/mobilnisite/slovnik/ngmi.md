---
slug: "ngmi"
url: "/mobilnisite/slovnik/ngmi/"
type: "slovnik"
title: "NGMI – Next Generation Mobile Intelligence"
date: 2026-01-01
abbr: "NGMI"
fullName: "Next Generation Mobile Intelligence"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ngmi/"
summary: "NGMI je rámec 3GPP pro rozšířenou inteligenci a analytiku mobilních sítí, zavedený ve vydání 13. Poskytuje standardizované mechanismy pro sběr, zpracování a využívání síťových dat k optimalizaci výkon"
---

NGMI je rámec 3GPP, zavedený ve vydání 13, který poskytuje standardizované mechanismy pro sběr a využívání síťových dat za účelem optimalizace výkonu, umožnění nových služeb a podpory automatizace.

## Popis

Next Generation Mobile Intelligence (NGMI) je komplexní rámec definovaný ve specifikacích 3GPP 33.179 a 33.180, zaměřený na architekturu a bezpečnostní aspekty inteligentního sběru a analytiky síťových dat. Stanovuje standardizovaná rozhraní a procedury pro získávání hodnotných poznatků ze síťových prvků, uživatelských zařízení (UE) a aplikací. Jádro architektury tvoří entity pro sběr dat ([DCE](/mobilnisite/slovnik/dce/)), které shromažďují nezpracovaná data, funkce pro analytiku a reportování (ARF), která tato data zpracovávají, a expoziční funkce, které bezpečně poskytují výslednou inteligenci autorizovaným konzumentům, jako jsou síťoví operátoři, poskytovatelé služeb třetích stran nebo vlastní systémy správy sítě.

NGMI funguje tak, že definuje strukturovaný datový model a sadu služebně orientovaných rozhraní (podobných těm používaným v 5G Core) pro vyžádání, doručení a odběr analytických reportů. Mezi klíčové zdroje dat patří výkonnostní měření, vzorce mobility, rádiové podmínky a statistiky využívání služeb. Analytické funkce na tato data aplikují algoritmy – které mohou být standardizované nebo specifické pro dodavatele – za účelem vytvoření poznatků, jako jsou předpovědi síťového zatížení, detekce anomálií, hodnocení uživatelského zážitku a zajištění kvality služeb. Bezpečnost je základním pilířem s mechanismy pro autentizaci, autorizaci a integritu dat, které zajišťují ochranu citlivých síťových a uživatelských dat v celém procesu sběru a vystavení.

Role rámce spočívá v oddělení generování inteligence od konkrétních síťových funkcí, čímž vytváří centralizovanou, opakovaně použitelnou schopnost pro celou síť. Umožňuje případy užití, jako je prediktivní vyvažování zátěže, automatizované řešení poruch, vylepšená správa kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)) a podpora operací síťového řezání. Poskytnutím společné 'inteligenční vrstvy' NGMI snižuje integrační složitost pro nové analytické aplikace a usnadňuje agilnější, softwarově řízený přístup ke správě a optimalizaci sítě, což je zásadní pro dynamické požadavky 5G a budoucích generací.

## K čemu slouží

NGMI byl vytvořen, aby řešil rostoucí složitost mobilních sítí a explozi dat, která generují. Před-5G sítě se často spoléhaly na proprietární, izolovaná řešení pro síťovou analytiku, což ztěžovalo získání holistického pohledu, integraci inteligence třetích stran nebo automatizaci složitých operací. Omezení těchto ad-hoc přístupů se stala úzkým hrdlem pro implementaci pokročilých konceptů, jako jsou samoorganizující se sítě ([SON](/mobilnisite/slovnik/son/)) ve velkém měřítku, a pro umožnění nových datově řízených služeb.

Primární motivací byla standardizace rozhraní a datových modelů pro síťovou inteligenci, čímž se podporuje ekosystém analytických aplikací a umožňuje efektivní interoperabilita mezi více dodavateli. Tato standardizace řeší problém závislosti na konkrétním dodavateli v oblasti síťové analytiky a umožňuje operátorům využívat nejlepší dostupná řešení. Dále poskytuje základní datovou infrastrukturu potřebnou k naplnění vize plně automatizované správy sítě a služeb bez lidského zásahu, což je klíčový cíl pro budoucí sítě.

Historicky byla inteligence zabudována do jednotlivých síťových funkcí. Vznik NGMI, souběžný s ranou standardizací 5G, odráží posun směrem k horizontálnější, služebně orientované architektuře, kde je inteligence sdílenou síťovou schopností. Řeší potřebu, aby sítě nebyly pouze přenosovými rourami, ale inteligentními platformami, které se mohou přizpůsobovat v reálném čase chování uživatelů, požadavkům aplikací a provozním podmínkám.

## Klíčové vlastnosti

- Standardizovaná služebně orientovaná rozhraní pro vyžádání a doručení analytiky
- Komplexní rámec pro sběr dat ze síťových funkcí a uživatelských zařízení
- Podpora reportování analytiky v reálném čase i historických dat
- Integrované bezpečnostní mechanismy pro autentizaci, autorizaci a ochranu dat
- Flexibilní analytický model podporující standardizované i dodavatelsky specifické algoritmy
- Umožňuje vystavení síťové inteligence autorizovaným interním i externím konzumentům

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [NGMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngmi/)
