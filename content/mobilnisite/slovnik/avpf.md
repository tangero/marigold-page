---
slug: "avpf"
url: "/mobilnisite/slovnik/avpf/"
type: "slovnik"
title: "AVPF – Audio-Video Profile with Feedback"
date: 2025-01-01
abbr: "AVPF"
fullName: "Audio-Video Profile with Feedback"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/avpf/"
summary: "AVPF je profil protokolu RTP (Real-time Transport Protocol), který vylepšuje multimediální komunikaci přidáním zpětnovazebních mechanismů pro audio a video proudy. Umožňuje přijímačům zasílat zprávy o"
---

AVPF je profil RTP, který přidává zpětnovazební mechanismy pro audio a video proudy, umožňující přijímačům zasílat zprávy o kvalitě odesílatelům za účelem adaptivního přizpůsobení přenosové rychlosti a zlepšení QoS v aplikacích reálného času.

## Popis

Audio-Video Profile with Feedback (AVPF) je profil protokolu [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) standardizovaný 3GPP v TS 26.922, který navazuje na základní profil Audio-Video Profile ([AVP](/mobilnisite/slovnik/avp/)). AVPF rozšiřuje základní rámec RTP/AVP o explicitní zpětnovazební mechanismy, které umožňují přijímačům zasílat zprávy o kvalitě zpět odesílatelům médií. Tato zpětná vazba je přenášena prostřednictvím paketů [RTCP](/mobilnisite/slovnik/rtcp/) (RTP Control Protocol), které fungují souběžně s hlavními proudy RTP médií. Profil definuje specifické typy paketů RTCP a časovací pravidla pro přenos zpětné vazby, čímž zajišťuje, že řídicí provoz zůstává v přijatelných šířkových limitech a zároveň poskytuje aktuální informace o stavu sítě a přijímače.

AVPF funguje prostřednictvím strukturovaného systému zpětné vazby, kde přijímače generují zprávy na základě pozorované ztráty paketů, zpoždění, jitteru a dalších metrik kvality. Tyto zprávy zahrnují pakety Receiver Report ([RR](/mobilnisite/slovnik/rr/)) s rozšířenou statistikou a také specializované zpětnovazební zprávy, jako je Picture Loss Indication ([PLI](/mobilnisite/slovnik/pli/)), Full Intra Request ([FIR](/mobilnisite/slovnik/fir/)) a Temporary Maximum Media Stream Bit Rate Request ([TMMBR](/mobilnisite/slovnik/tmmbr/)). Zpětnovazební zprávy dodržují definovaná časovací pravidla – buď okamžitou zpětnou vazbu pro naléhavé stavy (např. ztráta obrazu), nebo pravidelnou zpětnou vazbu pro průběžné monitorování kvality. To umožňuje odesílatelům přizpůsobit své kódovací parametry, jako je přenosová rychlost, snímková frekvence nebo funkce odolnosti proti chybám, v reakci na aktuální síťové podmínky.

Klíčové architektonické komponenty AVPF zahrnují cíl zpětné vazby, který identifikuje odesílatele médií nebo mezilehlý prvek přijímající zpětnou vazbu; zpětnovazební zprávy se specifickými formáty definovanými v [RFC](/mobilnisite/slovnik/rfc/) 4585; a časovací pravidla, která řídí, kdy lze zpětnou vazbu odeslat, aby se zabránilo přetížení šířky pásma RTCP. Profil podporuje jak bod-bodové, tak vícesměrové scénáře, což jej činí vhodným pro konferenční aplikace. V sítích 3GPP je AVPF integrován s multimediálními subsystémy, jako je IMS (IP Multimedia Subsystem), aby vylepšil služby jako VoLTE (Voice over LTE) a ViLTE (Video over LTE), kde je udržení konzistentní kvality při proměnných rádiových podmínkách klíčové.

Úloha AVPF v síti spočívá v překlenutí mezery mezi požadavky na kvalitu na aplikační vrstvě a podmínkami podkladového přenosu. Poskytnutím standardizovaného mechanismu pro zpětnou vazbu o kvalitě umožňuje adaptivní streamování, maskování chyb a řízení zahlcení bez nutnosti hluboké inspekce paketů médií síťovými prvky. Profil funguje ve spojení s dalšími funkcemi 3GPP, jako jsou QoS Class Identifiers (QCIs) a vyhrazené přenosy, aby zajistil kvalitu služeb reálného času od konce ke konci. Jeho zpětnovazební mechanismy jsou obzvláště cenné v mobilních prostředích, kde se rádiové podmínky mohou rychle měnit, což umožňuje multimediálním aplikacím udržovat přijatelný uživatelský zážitek navzdory variabilitě sítě.

## K čemu slouží

AVPF byl vytvořen, aby řešil omezení původního Audio-Video Profile (AVP), který poskytoval základní funkce RTP, ale postrádal standardizované zpětnovazební mechanismy pro adaptaci kvality v reálném čase. V raných multimediálních systémech aplikace buď používaly proprietární metody zpětné vazby, nebo fungovaly bez vstupu od přijímače, což vedlo k neoptimálnímu výkonu v ztrátových nebo přetížených sítích. Potřeba standardizovaného zpětnovazebního profilu se stala zjevnou s růstem videokonferencí reálného času a mobilních video služeb, kde jsou síťové podmínky nepředvídatelné a degradace kvality přímo ovlivňuje uživatelský zážitek.

Hlavním problémem, který AVPF řeší, je neschopnost odesílatelů médií přizpůsobit se síťovým podmínkám bez explicitní zpětné vazby od přijímačů. Před AVPF mohli odesílatelé problémy pouze odvozovat z pozorované ztráty paketů nebo vyžadovali signalizaci mimo pásmo, která byla často příliš pomalá nebo nekompatibilní mezi různými dodavateli. AVPF poskytuje standardizovaný kanál zpětné vazby v pásmu, který funguje napříč interoperabilními systémy, a umožňuje tak včasnou adaptaci na ztrátu paketů, změny šířky pásma a možnosti přijímače. To je obzvláště kritické v sítích 3GPP, kde jsou kolísání rádiových zdrojů běžná a efektivní využití šířky pásma je zásadní pro kvalitu služby a kapacitu sítě.

Historický kontext ukazuje, že AVPF se objevil souběžně s vývojem pokročilých video kodeků a expanzí služeb založených na IMS v sítích 3GPP. Jak sítě LTE umožnily kvalitní videohovory a streamování, potřeba robustních mechanismů adaptace kvality se stala prvořadou. AVPF na to reagoval poskytnutím zpětnovazebního rámce nezbytného pro funkce jako adaptivní streamování s proměnnou přenosovou rychlostí, odolnost proti chybám a řízení zahlcení ve standardizovaných multimediálních službách. Jeho vznik byl motivován pohybem průmyslu směrem k plně IP sítím, kde tradiční záruky kvality z okruhově přepínaných sítí již nebyly dostupné, což vyžadovalo nové paketové mechanismy pro udržení kvality služby.

## Klíčové vlastnosti

- Standardizované zpětnovazební zprávy RTCP pro hlášení kvality
- Podpora okamžité zpětné vazby pro naléhavé stavy, jako je ztráta obrazu
- Časovací pravidla pro řízení šířky pásma RTCP a prevenci zahlcení
- Kompatibilita s bod-bodovými i vícesměrovými scénáři
- Integrace se službami 3GPP IMS a multimédií
- Umožňuje adaptivní přenosovou rychlost, obnovu po chybách a řízení zahlcení

## Související pojmy

- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study

---

📖 **Anglický originál a plná specifikace:** [AVPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/avpf/)
