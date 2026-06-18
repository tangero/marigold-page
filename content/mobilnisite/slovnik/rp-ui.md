---
slug: "rp-ui"
url: "/mobilnisite/slovnik/rp-ui/"
type: "slovnik"
title: "RP-UI – RP User Information"
date: 2025-01-01
abbr: "RP-UI"
fullName: "RP User Information"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rp-ui/"
summary: "Datové pole v rámci zprávy Relay Protocol (RP) DATA, které přenáší vlastní obsah krátké zprávy (Short Message, SM). To zahrnuje text, binární data nebo protokolová data samotné SMS spolu s její přidru"
---

RP-UI je datové pole v rámci zprávy Relay Protocol DATA, které přenáší vlastní obsah a hlavičku krátké zprávy (Short Message) mezi SMSC a uživatelským zařízením (UE) prostřednictvím IMS.

## Popis

RP-UI ([RP](/mobilnisite/slovnik/rp/) User Information, informace RP od uživatele) je kontejner pro uživatelská data v rámci zprávy RP-DATA protokolu Relay Protocol. Zapouzdřuje kompletní krátkou zprávu (Short Message, [SM](/mobilnisite/slovnik/sm/)), která je vyměňována mezi centrem služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) a uživatelským zařízením (UE) v systému [SMS](/mobilnisite/slovnik/sms/) přes IMS (SMS-IP). RP-UI neobsahuje pouze prostý text zadaný uživatelem; obsahuje plně formátovanou jednotku dat transportního protokolu (Transport Protocol Data Unit, [TPDU](/mobilnisite/slovnik/tpdu/)), která zahrnuje hlavičku transportní vrstvy SMS ([TP](/mobilnisite/slovnik/tp/)) a vlastní uživatelská data. Hlavička TP vrstvy obsahuje pole jako TP-Protocol-Identifier, TP-Data-Coding-Scheme a TP-Validity-Period, zatímco pole uživatelských dat obsahuje zakódovaný text nebo binární informace.

Z architektonického pohledu je RP-UI nejvnitřnější vrstvou zásobníku protokolů SMS při přenosu přes IMS. Tento zásobník lze znázornit jako: zpráva [SIP](/mobilnisite/slovnik/sip/) -> zpráva RP (s [RP-MTI](/mobilnisite/slovnik/rp-mti/), RP-SMEA) -> pole RP-UI -> hlavička a data TP vrstvy. Když IP-SM-GW přijme SMS z klasické sítě prostřednictvím zprávy MAP_MT_FORWARD_SM, extrahuje SM (která je již TPDU) a umístí ji do pole RP-UI nově vytvořené zprávy RP-DATA. Tato zpráva RP-DATA je poté umístěna do těla požadavku SIP MESSAGE. Požadavek SIP je směrován přes jádro IMS k příjemci (UE). IMS klient v uživatelském zařízení extrahuje tělo SIP, identifikuje jej jako RP-DATA pomocí RP-MTI a následně zpracuje obsah RP-UI jeho předáním aplikační vrstvě SMS, která dekóduje TPDU, aby zobrazila zprávu uživateli.

Zpracování RP-UI je klíčové pro podporu pokročilých funkcí SMS. TP vrstva uvnitř RP-UI nese informace nezbytné pro zřetězené SMS (dlouhé zprávy rozdělené na více částí), flash SMS, Unicode pro mezinárodní znaky a kódování dat pro aplikační porty (používané např. pro služby jako stahování vyzvánění nebo WAP push). Protože RP-UI přenáší TPDU transparentně, všechny tyto klasické funkce SMS fungují beze změny i přes transport IMS. IP-SM-GW nemusí obsah RP-UI interpretovat ani upravovat; jeho role je primárně přenos mezi různými transportními mechanismy (MAP/SCCP/SS7 a SIP/IP). Tato transparentnost zajišťuje maximální kompatibilitu a zjednodušuje funkci brány.

## K čemu slouží

Pole RP-UI bylo vytvořeno za účelem poskytnutí transparentního a bezztrátového přenosového mechanismu pro kompletní datovou část SMS (TPDU) přes hranici mezi klasickou přepojovanou sítí SMS a novou paketovou sítí založenou na IMS. Před IMS byla TPDU přenášena v rámci protokolu MAP. Přechod na plně IP jádro vyžadoval metodu pro vložení této stávající, dobře definované struktury TPDU do signalizace založené na IP bez jakýchkoli úprav. Vrstva RP s polem RP-UI slouží jako tato standardizovaná obálka.

Tento návrh vyřešil kritický problém zachování funkčnosti služeb. SMS není jen prostý text; její TP vrstva podporuje širokou škálu funkcí (zřetězení, adresování portů, třídy zpráv, doby platnosti), které jsou zabudovány do struktury TPDU. Definováním RP-UI jako kontejneru, který uchovává celou, nezměněnou TPDU, zajistila 3GPP, že žádná z těchto funkcí nebude ztracena nebo narušena při směrování SMS provozu přes IMS. Umožnilo to čisté oddělení odpovědností: vrstva IMS (SIP) řeší řízení relace, vyhledávání a autentizaci, zatímco vrstva RP řeší dialog specifický pro SMS a RP-UI přenáší vlastní obsah zprávy. Tento přístup minimalizoval změny v rozsáhlém ekosystému SMSC a SMS klientů v koncových zařízeních, což umožnilo hladkou migrační cestu pro operátory a zaručilo konzistentní uživatelský zážitek bez ohledu na podkladovou transportní síť (CS nebo PS).

## Klíčové vlastnosti

- Zapouzdřuje kompletní jednotku dat transportního protokolu SMS (TPDU).
- Přenáší vlastní obsah uživatelské zprávy (text, binární data) a její hlavičku TP.
- Je IP-SM-GW přenášeno transparentně, bez interpretace nebo úprav.
- Umožňuje podporu všech klasických funkcí SMS (zřetězení, Unicode, flash SMS, adresování portů) přes IMS.
- Slouží jako datová část zprávy RP-DATA v rámci Relay Protocol.
- Doručováno koncově mezi aplikační vrstvou SMSC a aplikační vrstvou SMS v uživatelském zařízení (UE).

## Související pojmy

- [TPDU – Transport Protocol Data Unit](/mobilnisite/slovnik/tpdu/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)

## Definující specifikace

- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS

---

📖 **Anglický originál a plná specifikace:** [RP-UI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rp-ui/)
