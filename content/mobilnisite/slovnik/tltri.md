---
slug: "tltri"
url: "/mobilnisite/slovnik/tltri/"
type: "slovnik"
title: "TLTRI – T8 Long Term Transaction Reference ID"
date: 2025-01-01
abbr: "TLTRI"
fullName: "T8 Long Term Transaction Reference ID"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tltri/"
summary: "Jedinečný identifikátor používaný v rámci referenčního bodu T8 ke korelaci a správě dlouhodobých transakcí nebo relací mezi funkcí pro zpřístupnění servisních schopností (SCEF) a externími aplikačními"
---

TLTRI je jedinečný identifikátor používaný na referenčním bodě T8 ke korelaci dlouhodobých transakcí, jako je monitorování zařízení nebo doručování ne-IP dat, mezi SCEF a externími aplikačními servery (AS).

## Popis

T8 Long Term Transaction Reference ID (TLTRI) je klíčový identifikátor definovaný ve specifikacích 3GPP pro referenční bod T8, který spojuje funkci pro zpřístupnění servisních schopností ([SCEF](/mobilnisite/slovnik/scef/)) s externími aplikačními servery ([AS](/mobilnisite/slovnik/as/)) pro služby Cellular Internet of Things (CIoT). Rozhraní T8 používá protokol [HTTP](/mobilnisite/slovnik/http/)/2 a TLTRI se využívá v rámci těchto transakcí založených na HTTP. Jeho primární funkcí je jednoznačně označit a sledovat 'dlouhodobou transakci', která představuje probíhající interakci mezi AS a sítí pro konkrétní servisní požadavek týkající se UE nebo skupiny UE.

Z architektonického hlediska, když AS požaduje síťovou schopnost – například zřízení monitorovací události (např. pro upozornění při vstupu zařízení do určité oblasti), konfiguraci spouštěče zařízení (probouzející zpráva pro zařízení šetřící energii) nebo založení relace pro doručování ne-IP dat ([NIDD](/mobilnisite/slovnik/nidd/)) – SCEF vytvoří odpovídající prostředek a přiřadí mu TLTRI. Toto ID je pak vráceno AS v HTTP odpovědi (např. v hlavičce `Location` nebo těle odpovědi). TLTRI funguje jako manipulátor nebo klíč, který musí AS používat ve všech následných interakcích souvisejících s danou konkrétní transakcí. Například pro aktualizaci parametrů, dotaz na stav nebo odstranění monitorovací události AS zahrne TLTRI do [URL](/mobilnisite/slovnik/url/) adresy nebo hlaviček HTTP požadavku, což umožní SCEF správně identifikovat a manipulovat s příslušným síťovým prostředkem.

Jeho fungování je nedílnou součástí RESTful návrhu T8 [API](/mobilnisite/slovnik/api/). TLTRI je typicky vloženo do [URI](/mobilnisite/slovnik/uri/) prostředku, podle struktury jako `/{{apiRoot}}/{{apiName}}/{{apiVersion}}/{{resourceName}}/{{tltri}}`. Tento návrh je v souladu s principy [REST](/mobilnisite/slovnik/rest/), kde každá spravovaná entita (dlouhodobá transakce) je jednoznačně adresovatelný prostředek. SCEF je zodpovědná za generování TLTRI a zajištění jeho jedinečnosti v kontextu konkrétního API a instance SCEF. ID musí přetrvávat po celou dobu životnosti transakce, která může být velmi dlouhá (např. monitorovací událost pro stacionární měřič energie může trvat roky). Tato perzistence umožňuje síti efektivně udržovat stav pro nepravidelnou komunikaci IoT.

Jeho role spočívá v umožnění spolehlivých, stavových interakcí v prostředí z velké části bezstavového protokolu HTTP. Pro IoT, kde jsou relace dlouhodobé a události řídké, je udržování lehkého odkazu na straně AS (TLTRI) efektivnější než neustálé zasílání stavu ze sítě k AS nebo nutnost AS ukládat složité interní síťové identifikátory. Zjednodušuje logiku AS, poskytuje jasnou auditní stopu a je nezbytné pro správu prostředků SCEF, umožňující jí korelovat příchozí požadavky API s interními síťovými procedurami a kontexty UE, které ovlivňují. TLTRI je tedy základním kamenem pro škálovatelné zpřístupňování síťových schopností vertikálám IoT.

## K čemu slouží

TLTRI bylo vytvořeno k řešení specifických výzev správy dlouhodobých, asynchronních transakcí, které jsou vlastní službám IoT zpřístupňovaným přes rozhraní T8. Tradiční interakce mobilní sítě, jako hovory nebo relace prohlížení webu, jsou poměrně krátkodobé. Naproti tomu aplikace IoT často vyžadují, aby síť monitorovala zařízení po delší dobu (např. kvůli změně polohy) nebo držela spouštěč zařízení, dokud se zařízení nestane dostupným, což může trvat hodiny nebo dny. Jednoduché ID transakce používané pro krátké cykly HTTP požadavku/odpovědi bylo nedostatečné pro korelaci požadavků a odpovědí, které mohou být odděleny velkými časovými úseky.

Řeší problém korelace prostředků a správy životního cyklu v RESTful API navrženém pro komunikaci mezi stroji. Bez perzistentního, jedinečného identifikátoru, jako je TLTRI, by aplikační server neměl efektivní způsob, jak odkazovat na konkrétní monitorovací událost, kterou dříve vytvořil, když by ji později chtěl upravit nebo zrušit. Síť (SCEF) by také zápasila s mapováním příchozích požadavků API na správný interní stav relace. TLTRI poskytuje tento stabilní ukotvovací bod, oddělující dlouhodobý síťový stav od potenciálně bezstavového fungování AS.

Motivace pro jeho zavedení ve vydání Release 15 úzce souvisela se standardizací SCEF a rozhraní T8 jako primárního prostředku pro zpřístupňování síťových schopností CIoT (jako NIDD, Device Trigger a Monitoring) třetím stranám (AS) škálovatelným, bezpečným a programovatelným způsobem. V rámci širšího úsilí o umožnění masivního IoT musel návrh efektivně podporovat miliony takových dlouhodobých transakcí. TLTRI jako jednoduchý, avšak v kontextu SCEF globálně jedinečný identifikátor tuto potřebu naplňuje a umožňuje jasnou, jednoznačnou a efektivní správu těchto perzistentních síťově asistovaných služeb po celou dobu jejich potenciálně mnohaleté životnosti.

## Klíčové vlastnosti

- Jednoznačně identifikuje dlouhodobý transakční prostředek na rozhraní T8
- Generován a přiřazen SCEF při vytvoření síťového prostředku (např. monitorovací události)
- Používán aplikačním serverem (AS) jako manipulátor pro všechny následné operace (GET, UPDATE, DELETE) nad tímto prostředkem
- Vloženo do URI HTTP požadavku pro adresování prostředků v RESTful API voláních
- Přetrvává po celou dobu životnosti transakce, která mohou být dny, měsíce nebo roky
- Nezbytné pro správu asynchronních, dlouhodobých služeb IoT, jako je monitorování a spouštění zařízení

## Související pojmy

- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)

## Definující specifikace

- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [TLTRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tltri/)
