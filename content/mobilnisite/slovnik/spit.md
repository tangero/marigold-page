---
slug: "spit"
url: "/mobilnisite/slovnik/spit/"
type: "slovnik"
title: "SPIT – Spam over IP Telephony"
date: 2025-01-01
abbr: "SPIT"
fullName: "Spam over IP Telephony"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spit/"
summary: "Nevyžádané, hromadné, automatizované nebo podvodné hlasové či videohovory přenášené přes IP telekomunikační sítě, jako jsou VoLTE a VoNR. Jde o telekomunikační ekvivalent emailového spamu, který předs"
---

SPIT je přenos nevyžádaných, hromadných, automatizovaných nebo podvodných hlasových či videohovorů přes telekomunikační sítě založené na IP protokolu, což představuje výzvy v oblasti zabezpečení, ochrany soukromí a efektivity sítě.

## Popis

Spam over IP Telephony (SPIT) označuje přenos nevyžádané a často škodlivé komunikace – primárně hlasových hovorů, ale potenciálně i videohovorů a instantních zpráv – přes telekomunikační služby založené na internetovém protokolu (IP). V kontextu 3GPP cílí tento fenomén na služby jako Voice over LTE (VoLTE) a Voice over NR (VoNR). SPIT hovory jsou typicky generovány automaticky softwarem („spamboty“) a jejich spektrum sahá od telemarketingu po phishingové pokusy nebo podvody. IP povaha IMS telekomunikace ji činí náchylnou k podobným formám zneužití jako email a webový provoz, avšak s přidaným prvkem reálného času a potenciálem pro bezprostřednější sociotechnické útoky.

3GPP řeší SPIT prostřednictvím rámce definovaného v TS 33.937, který stanovuje bezpečnostní požadavky a potenciální protiopatření v architektuře IP Multimedia Subsystem (IMS). Obrana je vícevrstvá. Primární součástí je analýza signalizace, zejména zpráv [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) používaných k navázání hovorů. Síťové elementy jako Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) mohou kontrolovat hlavičky a parametry SIP zpráv, aby odhalily vzorce typické pro spam, jako je vysoká frekvence hovorů z jednoho zdroje, chybně formátované zprávy nebo podezřelé identity volajícího. Rámec také definuje roli specializované anti-SPIT entity, která může aplikovat složitější heuristické, reputační nebo challenge-response mechanismy.

Mezi potenciální techniky zmírnění dopadů patří černé/bílé listiny, šedé listování (dočasné odmítnutí hovoru a čekání na opakovaný pokus od legitimního klienta), výpočetní úlohy (vyžadování po volajícím zařízení, aby vyřešilo jednoduchou výpočetní úlohu a prokázalo, že nejde o bota) a komunikace založená na souhlasu, kdy jsou povoleny pouze hovory od účastníků v seznamu kontaktů volaného. Rámec je navržen jako flexibilní, což operátorům umožňuje implementovat kombinaci těchto opatření. Dále bere v úvahu předpisy na ochranu soukromí a zajišťuje, aby anti-SPIT zpracování nelegálně nemonitorovalo obsah hovorů. Cílem je integrovat tyto ochrany plynule do IMS toku hovoru, aby byly pokusy o SPIT zablokovány nebo označeny ještě před dosažením koncového zařízení uživatele.

## K čemu slouží

SPIT se stal významnou hrozbou s migrací tradičních okruhově přepínaných hlasových služeb na plně IP sítě, jako je IMS. Zatímco IP telekomunikace přinesla výhody v nákladech a inovacích služeb, zdědila také zranitelnosti internetu, kde je spam všudypřítomným problémem. Tradiční telekomunikace měla určitou inherentní ochranu díky své uzavřené povaze a modelu platby za hovor, ale VoLTE/VoNR, využívající otevřenou [SIP](/mobilnisite/slovnik/sip/) signalizaci přes IP, snížily bariéru pro masové automatizované útoky voláním. To vytvořilo nové problémy: obtěžování uživatelů a narušování soukromí, zvýšené zatížení sítě signalizací z neúspěšných pokusů o hovor a potenciál pro rozsáhlé podvody.

Práce 3GPP na SPIT, zahájená ve Release 9, byla motivována potřebou proaktivně zabezpečit hlasové služby založené na IMS a udržet důvěru uživatelů. Bez standardizovaných protiopatření by si každý operátor vyvíjel proprietární řešení, což by vedlo k fragmentaci a potenciálním problémům s interoperabilitou. Standardizace poskytuje společnou sadu požadavků a architektonických směrnic, což umožňuje výrobcům vyvíjet kompatibilní řešení a operátorům nasazovat efektivní, více-dodavatelské anti-SPIT ekosystémy. Řeší jedinečné výzvy komunikace v reálném čase, kde musí být filtrování provedeno s minimálním zpožděním, aby nedocházelo k ovlivnění času navázání legitimních hovorů, a vyvažuje tak zabezpečení s kvalitou služby.

## Klíčové vlastnosti

- Rámec pro zmírnění dopadů nevyžádaných hlasových/videohovorů založených na IMS
- Analýza vzorců SIP signalizace pro detekci spamu
- Podpora různých technik: černé listiny, výpočetní úlohy, šedé listování
- Definice architektonických rolí pro anti-SPIT entity v IMS
- Zaměření na ochranu soukromí uživatele během anti-SPIT zpracování
- Použitelnost pro VoLTE, VoNR a další komunikační služby IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TR 33.937** (Rel-19) — Protection against Unsolicited Communication in IMS

---

📖 **Anglický originál a plná specifikace:** [SPIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/spit/)
