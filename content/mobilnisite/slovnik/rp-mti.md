---
slug: "rp-mti"
url: "/mobilnisite/slovnik/rp-mti/"
type: "slovnik"
title: "RP-MTI – RP Message Type Indicator"
date: 2025-01-01
abbr: "RP-MTI"
fullName: "RP Message Type Indicator"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rp-mti/"
summary: "Pole v přenosovém protokolu (RP) používané při doručování služby krátkých textových zpráv (SMS) přes IP multimediální subsystém (IMS). Identifikuje konkrétní typ přenášené zprávy RP, například datovou"
---

RP-MTI je pole v přenosovém protokolu (Relay Protocol) používaném pro SMS přes IMS, které identifikuje typ zprávy RP, například datovou zprávu nebo hlášení o chybě, aby umožnilo správné směrování a zpracování.

## Popis

RP-MTI (indikátor typu zprávy [RP](/mobilnisite/slovnik/rp/)) je klíčový informační prvek ve vrstvě přenosového protokolu (RP), která funguje jako část architektury [SMS](/mobilnisite/slovnik/sms/) přes IP (SMS-IP) definované 3GPP. Vrstva RP je zodpovědná za spolehlivý přenos krátkých zpráv mezi centrem služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) a mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelským zařízením (UE), zejména když zpráva prochází IP sítí IMS. RP-MTI je povinné pole v hlavičce RP a jeho hodnota určuje formát a interpretaci celé zprávy RP. V podstatě funguje jako identifikátor příkazu, který říká přijímající entitě – například IP bráně pro krátké zprávy ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)) nebo samotnému UE – jak zpracovat přidružená datová část.

Technicky je RP-MTI kódový bod v datové jednotce protokolu RP ([PDU](/mobilnisite/slovnik/pdu/)). Když entita vytváří zprávu RP, nastaví RP-MTI na předdefinovanou hodnotu odpovídající účelu zprávy. Například hodnota RP-MTI může indikovat zprávu RP-DATA, která nese vlastní uživatelská data SMS (textový nebo binární obsah). Jiná hodnota indikuje RP-ACK, což je kladné potvrzení dříve přijaté zprávy RP-DATA. Naopak zpráva RP-ERROR, indikovaná svou specifickou hodnotou RP-MTI, signalizuje selhání při zpracování předchozího příkazu RP. Přijímací síťový uzel nejprve analyzuje toto pole, aby určil následnou logiku parsování zbytku zprávy RP, včetně zpracování dalších polí, jako je [RP-SMEA](/mobilnisite/slovnik/rp-smea/) (adresa odesílatele) a [RP-UI](/mobilnisite/slovnik/rp-ui/) (uživatelská datová část).

Jeho role je zásadní pro správu relací a ošetřování chyb při doručování SMS. V architektuře SMS založené na IMS jsou zprávy vrstvy RP zapouzdřeny do zpráv SIP (Session Initiation Protocol) pro přenos. IP-SM-GW zprostředkovává interoperabilitu mezi signalizací SMS založenou na starším protokolu MAP (Mobile Application Part)/SS7 a signalizací IMS založenou na SIP. Když IP-SM-GW přijme SMS ze SMSC přes MAP, vytvoří příslušnou zprávu RP (např. RP-DATA), odpovídajícím způsobem nastaví RP-MTI a vloží ji do požadavku SIP MESSAGE, který má být směrován do UE. IMS klient v UE extrahuje zprávu RP, přečte RP-MTI a na základě jeho hodnoty buď zpracuje SMS pro zobrazení, vygeneruje RP-ACK k odeslání zpět přes SIP, nebo řeší chybový stav. Tím je zajištěno, že end-to-end procedury SMS, včetně doručovacích hlášení a oznámení o selhání, fungují správně v paketové doméně.

## K čemu slouží

RP-MTI byl zaveden, aby poskytl strukturovaný a jednoznačný mechanismus pro identifikaci různých procedurálních zpráv ve vrstvě přenosového protokolu (RP), což je nezbytné pro interoperabilitu tradičních SMS v přepojování okruhů s IP multimediálním subsystémem (IMS). Před SMS založenými na IMS bylo doručování SMS silně závislé na signalizační síti SS7 a protokolu MAP, kde byly typy zpráv implicitně chápány v kontextu operací MAP. Avšak s migrací na plně IP sítě (IP multimediální subsystém jádra sítě, IMS) vznikla potřeba přenášet signalizaci SMS transparentně přes SIP, což je protokol pro řízení relací, který nebyl původně navržen pro SMS. Vrstva RP a konkrétně RP-MTI byly definovány, aby zachovaly stavovou, příkaz/odpověď povahu doručování SMS v rámci rámce zpráv SIP orientovaného na bezstavovost.

Jeho zavedení vyřešilo problém, jak signalizovat záměr zprávy související se SMS mezi sítí a UE při použití SIP jako transportu. Bez jasného indikátoru, jako je RP-MTI, by SIP entita nedokázala rozlišit mezi zprávou nesoucí nový obsah SMS, potvrzením o doručení nebo hlášením o selhání. To by narušilo základní funkce SMS, jako jsou doručovací hlášení a mechanismy opakování. RP-MTI umožňuje IP-SM-GW a UE vést stejný logický dialog RP, který by probíhal v síti s přepojováním okruhů, ale nyní zapouzdřený v rámci dialogů SIP. To umožňuje hladkou konvergenci služeb zasílání zpráv, podporuje přechod operátora na plně IP sítě při zachování zpětné kompatibility s rozsáhlou stávající infrastrukturou SMS a očekáváními uživatelů.

## Klíčové vlastnosti

- Definuje operační záměr datové jednotky protokolu RP (PDU).
- Umožňuje rozlišení mezi typy zpráv RP, jako jsou RP-DATA, RP-ACK a RP-ERROR.
- Povinné pole v hlavičce RP pro všechny zprávy RP.
- Zajišťuje, že přijímající entita použije správnou logiku parsování a zpracování.
- Umožňuje spolehlivé procedury přenosu SMS (potvrzení, hlášení chyb) přes IMS.
- Kritické pro interoperabilitu mezi entitami SMSC založenými na MAP a entitami IMS založenými na SIP.

## Související pojmy

- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [RP-UI – RP User Information](/mobilnisite/slovnik/rp-ui/)

## Definující specifikace

- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS

---

📖 **Anglický originál a plná specifikace:** [RP-MTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rp-mti/)
