---
slug: "dppk"
url: "/mobilnisite/slovnik/dppk/"
type: "slovnik"
title: "DPPK – MCData Payload Protection Key"
date: 2026-01-01
abbr: "DPPK"
fullName: "MCData Payload Protection Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/dppk/"
summary: "Kryptografický klíč používaný ve službách 3GPP Mission Critical Data (MCData) k šifrování a ochraně integrity aplikačních přenosových dat. Zajišťuje důvěrnost a integritu dat pro citlivou komunikaci k"
---

DPPK je kryptografický klíč používaný ve službách 3GPP MCData k šifrování a ochraně integrity aplikačních přenosových dat, čímž zajišťuje důvěrnost a integritu dat pro citlivou komunikaci klíčovou pro plnění misí.

## Popis

MCData Payload Protection Key (DPPK) je symetrický kryptografický klíč definovaný v rámci bezpečnostní architektury 3GPP pro služby Mission Critical Services. Je generován a spravován jako součást hierarchie klíčů vytvořené během autorizace služby a nastavení relace pro MCData. DPPK je konkrétně používán na aplikační vrstvě k ochraně přenosových dat uživatelských dat vyměňovaných mezi klienty MCData. Jeho primární funkcí je poskytovat zabezpečení typu end-to-end pro samotné přenášené informace klíčové pro misi, jako jsou data o poloze, soubory nebo textové zprávy, nezávisle na zabezpečení podléhající přenosové sítě (jako [IPsec](/mobilnisite/slovnik/ipsec/) nebo TLS).

Klíč je odvozen v bezpečném prostředí systému MCData, často za účasti Key Management Function (KMF) nebo serveru MCData. Proces odvození typicky používá kořenový klíč specifický pro službu MCData a další parametry specifické pro relaci. Po odvození je DPPK bezpečně poskytnut autorizovaným klientským aplikacím MCData. Klientská aplikace následně tento klíč používá se specifikovanou sadou kryptografických algoritmů (např. AES-GCM) k zašifrování a ochraně integrity přenosových dat před odesláním. Přijímající klient, který disponuje stejným DPPK, může data dešifrovat a ověřit jejich integritu.

Z architektonického hlediska DPPK funguje v rámci bezpečnostní vrstvy aplikace MCData. Je klíčovou součástí bezpečnostního modelu typu end-to-end pro MCData, který doplňuje zabezpečení typu hop-by-hop poskytované sítí 3GPP. Životní cyklus klíče – včetně generování, distribuce, používání a odstranění – je přísně kontrolován systémovými politikami MCData, aby se zabránilo neoprávněnému přístupu a zajistil forward secrecy. Jeho úlohou je garantovat, že data klíčová pro misi zůstanou důvěrná a nezměněná, i když jsou jiné segmenty sítě kompromitovány, což je základním požadavkem pro komunikaci v oblasti veřejné bezpečnosti a kritické infrastruktury.

## K čemu slouží

DPPK byl zaveden, aby řešil přísné bezpečnostní požadavky služeb Mission Critical Data, které jsou nezbytné pro veřejnou bezpečnost, zásahové řízení a kritické průmyslové operace. Tradiční zabezpečení mobilních sítí (např. [NAS](/mobilnisite/slovnik/nas/) a [AS](/mobilnisite/slovnik/as/) security v 5G) primárně chrání signalizaci a data uživatelské roviny mezi zařízením a sítí, ale neposkytuje skutečné zabezpečení typu end-to-end na aplikační vrstvě mezi uživateli. Pro citlivou komunikaci klíčovou pro plnění misí je potřeba chránit samotný obsah dat před potenciálními hrozbami uvnitř sítě poskytovatele služeb nebo před kompromitovanými síťovými prvky.

Před jeho standardizací systémy pro komunikaci klíčovou pro misi často spoléhaly na proprietární nebo externí bezpečnostní řešení, která nebyla integrována s ekosystémem 3GPP, což vedlo k problémům s interoperabilitou a složitou správou klíčů. Vytvoření DPPK jako součásti bezpečnostního rámce 3GPP MCData ve verzi 15 poskytlo standardizovaný, nativní mechanismus pro ochranu přenosových dat. Řeší problém zajištění důvěrnosti a integrity dat pro aplikace MCData napříč různými dodavateli a sítěmi, což umožňuje bezpečnou interoperabilitu pro složky záchranného systému operující na komerčních sítích 3GPP. Jeho existence byla motivována celosvětovým tlakem směrem k misi kritické komunikaci založené na širokopásmových technologiích (jako služby 3GPP [MCX](/mobilnisite/slovnik/mcx/)), která má nahradit nebo rozšířit starší úzkopásmové systémy, což si vyžádalo robustní, standardizované zabezpečení šité na míru aplikační vrstvě.

## Klíčové vlastnosti

- Poskytuje šifrování typu end-to-end pro aplikační přenosová data služby MCData
- Zajišťuje integritu dat pro výměnu informací klíčových pro plnění misí
- Funguje jako součást definované hierarchie klíčů 3GPP MCData
- Podporuje bezpečné odvození a distribuci prostřednictvím entit systému MCData
- Umožňuje flexibilitu ve volbě kryptografických algoritmů dle specifikací 3GPP
- Nezávisí na bezpečnostních mechanismech podléhající přenosové sítě

## Definující specifikace

- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [DPPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/dppk/)
