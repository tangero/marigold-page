---
slug: "uc"
url: "/mobilnisite/slovnik/uc/"
type: "slovnik"
title: "UC – Unsolicited Communication"
date: 2025-01-01
abbr: "UC"
fullName: "Unsolicited Communication"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uc/"
summary: "Komunikace iniciovaná bez předchozího souhlasu nebo vyžádání od příjemce, často odkazující na nežádoucí zprávy jako spam nebo podvody. V 3GPP zahrnuje mechanismy pro detekci, prevenci a zmírnění takov"
---

UC je typ komunikace iniciované bez předchozího souhlasu příjemce, například spam, jehož detekci, prevenci a zmírnění v rámci mobilních sítí mají za cíl standardy 3GPP.

## Popis

Nevyžádaná komunikace (Unsolicited Communication, UC) v kontextech 3GPP označuje jakoukoli komunikaci – například hovory, [SMS](/mobilnisite/slovnik/sms/) nebo datové zprávy – která je iniciována bez výslovného souhlasu nebo předchozího vyžádání příjemce. Typicky to zahrnuje spam, phishing, podvody a další škodlivý nebo nežádoucí provoz, který může zhoršit uživatelský zážitek, spotřebovávat síťové zdroje a představovat bezpečnostní rizika. Standardy 3GPP řeší UC prostřednictvím vícefázového přístupu zahrnujícího mechanismy detekce, prevence a zmírnění integrované do jádra sítě a uživatelského zařízení.

Architektura pro zpracování UC zahrnuje několik síťových funkcí a rozhraní. Mezi klíčové komponenty patří Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro data účastníka, Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) pro uplatňování politik souvisejících s UC a v 5G Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) pro řízení relace. Dále mohou pomáhat s filtrováním signalizace mezi sítěmi specializované bezpečnostní funkce jako Security Edge Protection Proxy ([SEPP](/mobilnisite/slovnik/sepp/)). Detekce UC často spoléhá na analytické nástroje, které monitorují vzorce provozu, pověst odesílatele a podpisy obsahu k identifikaci podezřelých aktivit.

Jak to funguje: Při pokusu o komunikaci může síť uplatnit politiky na základě faktorů, jako je identita odesílatele, cíl a historické chování. Například, pokud je číslo označeno jako spam, síť může hovor nebo zprávu zablokovat, přesměrovat do složky se spamem nebo upozornit uživatele. V pokročilejších implementacích analyzují algoritmy strojového učení data v reálném čase, aby adaptivně detekovaly nové vzorce UC. UE se také může účastnit hlášením nežádoucí komunikace nebo aplikací lokálních filtrů. Tato společná snaha sítě a zařízení pomáhá minimalizovat dopad UC při zachování legitimních komunikačních toků.

## K čemu slouží

Standardizace UC v 3GPP byla hnána rostoucím problémem mobilního spamu, podvodů a obtěžujících komunikací, které narušují důvěru uživatelů a efektivitu sítě. Před systematickými přístupy se operátoři spoléhali na základní filtrování nebo aplikace třetích stran, což vedlo k nekonzistentní ochraně a zranitelnosti vůči vyvíjejícím se hrozbám, jako je smishing ([SMS](/mobilnisite/slovnik/sms/) phishing) nebo automatické hovory. Nedostatek interoperability bránil úsilí mezi operátory v efektivním boji proti UC.

3GPP začala řešit UC ve vydání 9, zpočátku se zaměřovala na definice rámce a základní mechanismy. Účelem je poskytnout standardizované, na síť zaměřené řešení, které dokáže proaktivně identifikovat a blokovat nežádoucí komunikaci, čímž chrání účastníky a šetří síťové zdroje. Řeší problémy jako je obtěžování uživatelů, finanční podvody a zahlcení sítě způsobené hromadným nevyžádaným provozem.

V následujících vydáních se rozsah rozšířil o nové typy komunikace (např. [RCS](/mobilnisite/slovnik/rcs/), zprávy IoT) a sofistikované útoky. Motivace zahrnuje regulatorní tlaky (např. GDPR, zákony proti spamu) a potřeby průmyslu pro bezpečný mobilní ekosystém. Integrací zpracování UC do síťové architektury umožňuje 3GPP škálovatelnou, efektivní ochranu, která se přizpůsobuje novým hrozbám, čímž zvyšuje celkovou kvalitu služeb a bezpečnost.

## Klíčové vlastnosti

- Rámec pro detekci a zmírnění nevyžádaných hovorů, SMS a zpráv
- Integrace s funkcemi jádra sítě (např. UDM, PCF) pro vynucování politik
- Podpora správy souhlasu účastníka a nastavení preferencí
- Analytika a rozpoznávání vzorů pro adaptivní identifikaci UC
- Mechanismy spolupráce mezi operátory pro sdílení informací o hrozbách
- Možnosti hlášení s asistencí UE a lokální filtrování

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 32.511** (Rel-19) — ANR Management Concepts & Requirements
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 33.838** (Rel-11) — Study on Protection against Unsolicited Communication for IMS
- **TR 33.937** (Rel-19) — Protection against Unsolicited Communication in IMS

---

📖 **Anglický originál a plná specifikace:** [UC na 3GPP Explorer](https://3gpp-explorer.com/glossary/uc/)
