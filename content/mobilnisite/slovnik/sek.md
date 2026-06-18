---
slug: "sek"
url: "/mobilnisite/slovnik/sek/"
type: "slovnik"
title: "SEK – SS7 security gateway Encryption Key"
date: 2025-01-01
abbr: "SEK"
fullName: "SS7 security gateway Encryption Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sek/"
summary: "SEK je kryptografický klíč používaný k zabezpečení signalizačního provozu mezi bránami zabezpečení SS7 (SEG) v sítích 3GPP. Je klíčový pro ochranu důvěrnosti a integrity signalizačních zpráv založenýc"
---

SEK je kryptografický klíč používaný k zajištění důvěrnosti a integrity signalizačních zpráv SS7 mezi bránami zabezpečení SS7 (SS7 security gateways) přes nedůvěryhodné IP sítě.

## Popis

Šifrovací klíč brány zabezpečení [SS7](/mobilnisite/slovnik/ss7/) (SEK) je základní součástí rámce zabezpečení síťové domény ([NDS](/mobilnisite/slovnik/nds/)) definovaného 3GPP, konkrétně popsaného v TS 33.204. Funguje v rámci architektury bran zabezpečení SS7 ([SEG](/mobilnisite/slovnik/seg/)), což jsou síťové uzly zodpovědné za zabezpečení provozu signalizačního systému č. 7 (SS7) při přenosu přes IP sítě, například těch, které propojují různé mobilní operátory pro roaming. SEK je symetrický kryptografický klíč, což znamená, že stejný klíč používají obě spárované SEG na koncích zabezpečeného tunelu pro šifrování i dešifrování. Jeho primární funkcí je poskytnout důvěrnost signalizačních zpráv zapouzdřených v protokolu [NDS/IP](/mobilnisite/slovnik/nds-ip/). Klíč se používá ve spojení se specifickými šifrovacími algoritmy standardizovanými 3GPP k zašifrování obsahu signalizačních paketů.

Generování, distribuce a správa klíče SEK jsou kritické bezpečnostní operace. Typicky se klíče SEK vytvářejí pomocí protokolu pro správu klíčů, často integrovaného s protokolem Internet Key Exchange ([IKE](/mobilnisite/slovnik/ike/)), který se používá k navázání zabezpečených asociací ([SA](/mobilnisite/slovnik/sa/)) [IPsec](/mobilnisite/slovnik/ipsec/) mezi SEG. Životní cyklus klíče SEK zahrnuje jeho vytvoření, aktivaci pro použití v rámci SA IPsec, periodickou obnovu (re-keying) pro omezení množství dat zašifrovaných pod jedním klíčem (osvědčený bezpečnostní postup) a případné smazání. Klíč se nikdy nepřenáší po síti v otevřené podobě; namísto toho se šifrovací materiál bezpečně vyměňuje pomocí asymetrické kryptografie během fáze vyjednávání IKE.

V rámci architektury NDS/IP se SEK aplikuje na vrstvě IPsec. Když SEG přijme zprávu SS7 (např. zprávu [MAP](/mobilnisite/slovnik/map/) nebo CAP) určenou partnerské síti, zapouzdří ji do IP paketu. Před odesláním použije mechanismus IPsec aktivní klíč SEK k zašifrování celého užitečného zatížení IP paketu (které obsahuje signalizaci SS7), čímž zajistí, že i v případě zachycení paketu zůstanou citlivé signalizační informace důvěrné. Příjemající SEG, která má stejný klíč SEK, užitečné zatížení dešifruje, aby získala původní zprávu SS7 pro další zpracování. Tento proces chrání před hrozbami, jako je odposlech signalizace, podvody nebo sledování polohy, které by mohly být provedeny útokem na signalizační propojení mezi operátory.

## K čemu slouží

SEK byl zaveden k řešení významných bezpečnostních slabin vlastních tradiční signalizační síti SS7, když začala používat IP přenos. Historicky byly sítě SS7 uzavřené, okruhově přepínané systémy považované za bezpečné díky fyzické izolaci. Migrace na přenos založený na IP (pomocí protokolů SIGTRAN) z důvodu nákladů a flexibility však vystavila signalizaci SS7 široké škále útoků pocházejících z internetu. Bez šifrování by signalizační zprávy obsahující citlivá data účastníků (jako aktualizace polohy, nastavení přesměrování hovorů a autentizační vektory) mohly být snadno odposlechnuty, upraveny nebo vloženy na IP propojení mezi operátory.

Vytvoření rámce NDS/IP a konkrétně klíče SEK bylo motivováno potřebou vytvořit standardizovanou, robustní bezpečnostní vrstvu pro tuto kritickou komunikaci mezi operátory. Řeší problém, jak zachovat důvěrnost a integritu starší signalizace SS7 v moderním, otevřeném IP prostředí. SEK umožňuje operátorům využívat nákladově efektivní IP sítě pro přenos signalizace, aniž by byla ohrožena bezpečnostní a soukromí požadovaná pro telekomunikační služby. Tvoří kryptografický základ, který brání odposlechu roamingových transakcí a blokuje neoprávněnou manipulaci se signalizací, která by mohla vést k podvodům nebo narušení služeb.

## Klíčové vlastnosti

- Symetrický šifrovací klíč pro zajištění důvěrnosti provozu SS7-over-IP (NDS/IP)
- Integrální součást rámce zabezpečení síťové domény 3GPP (NDS/IP)
- Používán v rámci protokolu IPsec Encapsulating Security Payload (ESP)
- Vytvářen a spravován pomocí zabezpečených protokolů pro výměnu klíčů, jako je IKEv1/IKEv2
- Podléhá periodické obnově (re-keying) pro omezení kryptografické expozice
- Aplikován na bázi zabezpečené asociace (SA) mezi spárovanými bránami zabezpečení SS7 (SEG)

## Související pojmy

- [NDS/IP – Network Domain Security for IP based Protocols](/mobilnisite/slovnik/nds-ip/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [IKE – Internet Key Exchange](/mobilnisite/slovnik/ike/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SEK na 3GPP Explorer](https://3gpp-explorer.com/glossary/sek/)
