---
slug: "wv"
url: "/mobilnisite/slovnik/wv/"
type: "slovnik"
title: "WV – Wireless Village"
date: 2025-01-01
abbr: "WV"
fullName: "Wireless Village"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wv/"
summary: "Průmyslová iniciativa, později integrovaná do 3GPP, která definovala univerzální protokol pro služby okamžitého zasílání zpráv a přítomnosti (IMPS) v mobilních sítích. Jejím cílem bylo vytvořit intero"
---

WV je integrovaná iniciativa 3GPP, která definovala univerzální protokol pro interoperabilní služby okamžitého zasílání zpráv a přítomnosti napříč sítěmi a zařízeními.

## Popis

Wireless Village (WV) nebyla technologie vynalezená 3GPP, ale specifikace nezávislého průmyslového fóra, která byla následně přijata a rozvíjena v rámci 3GPP, především pod hlavičkou IP Multimedia Subsystem (IMS). Definovala Wireless Village Protocol, komplexní sadu protokolů pro Instant Messaging and Presence Service (IMPS). Architektura je typu klient-server, kde WV klient na mobilním zařízení komunikuje s WV serverem v síti operátora. Soubor protokolů pokrývá několik klíčových funkčních oblastí: Přítomnost (Presence), která umožňuje uživatelům publikovat svou dostupnost a stav (online, zaneprázdněn, pryč) a odebírat stavy ostatních; Okamžité zasílání zpráv (Instant Messaging) podporující individuální a skupinové chatové relace s potvrzeními o doručení; a Správa skupin (Group Management) pro vytváření a správu seznamů kontaktů či chatovacích místností.

Protokol funguje nad standardním IP transportem, typicky využívá efektivní binární protokol přizpůsobený mobilnímu prostředí. WV Server funguje jako centrální uzel, který spravuje autentizaci uživatelů, směruje zprávy mezi klienty, ukládá informace o přítomnosti a zpracovává členství ve skupinách. Rozhraní má k dalším síťovým prvkům, jako jsou Home Location Registers ([HLR](/mobilnisite/slovnik/hlr/)) pro data účastníků a případně [SMS](/mobilnisite/slovnik/sms/) brány pro záložní řešení nebo notifikace. Komunikace klient-server zahrnuje sérii transakcí požadavek-odpověď pro akce jako odeslání zprávy, aktualizace stavu přítomnosti nebo načtení seznamu kontaktů. Klíčovým technickým aspektem byl důraz na lehkost a vhodnost pro omezenou šířku pásma a výpočetní výkon mobilních telefonů v éře 2.5G/3G.

V rámci ekosystému 3GPP byly specifikace WV absorbovány a staly se základem pro služby zasílání zpráv a přítomnosti založené na IMS, zejména ovlivnily Open Mobile Alliance ([OMA](/mobilnisite/slovnik/oma/)) SIMPLE [IM](/mobilnisite/slovnik/im/) a později standardy 3GPP Joyn/[RCS](/mobilnisite/slovnik/rcs/) (Rich Communication Services). Jejím úkolem bylo poskytnout standardizovanou, interoperabilní alternativu k proprietárním mobilním chatovacím aplikacím a definovat, jak lze přítomnost – klíčový prvek mnoha komunikačních služeb – implementovat způsobem vhodným pro operátorské sítě, bezpečně a s možností účtování.

## K čemu slouží

Wireless Village byla vytvořena na konci 90. let a počátku 21. století, aby vyřešila problém fragmentovaných, proprietárních služeb okamžitého zasílání zpráv na mobilních telefonech. V té době byly internetové [IM](/mobilnisite/slovnik/im/) služby (jako AOL Instant Messenger) populární na [PC](/mobilnisite/slovnik/pc/), ale nebyly navrženy pro mobilní prostředí se svými specifickými výzvami: omezená velikost obrazovky, přerušované připojení a požadavky operátorů na zabezpečení a účtování. Každý výrobce telefonů nebo operátor vyvíjel své vlastní uzavřené řešení, což vedlo k nedostatku interoperability; uživatelé na různých sítích nebo s různými telefony si nemohli vyměňovat zprávy.

Iniciativa si kladla za cíl vytvořit univerzální, otevřený standard pro mobilní IM a přítomnost, který by umožnil jakémukoli kompatibilnímu zařízení na jakékoli kompatibilní síti vyměňovat zprávy a informace o přítomnosti. To by operátorům umožnilo nabízet hodnotnou službu zvyšující loajalitu, konkurovat novým [OTT](/mobilnisite/slovnik/ott/) hráčům a využít své vztahy v oblasti identity účastníka a účtování. Standardizací protokolu také snížila vývojové náklady pro výrobce telefonů. Integrace její práce do 3GPP (počínaje Release 6 v kontextu IMS) byla motivována potřebou průmyslu po jednotném, globálně uznávaném standardu pro služby reálného času jako součásti vývoje směrem k plně IP síti. Řešila omezení SMS (která postrádala přítomnost a relace založené na chatu) a proprietárních řešení (která postrádala škálovatelnost a interoperabilitu).

## Klíčové vlastnosti

- Standardizovaný protokol pro okamžité zasílání zpráv v mobilních sítích (1 ku 1 a skupinové)
- Komplexní služba přítomnosti pro publikování a odebírání stavu dostupnosti uživatele
- Schopnosti správy skupin a seznamů kontaktů
- Návrh pro efektivní provoz přes mobilní sítě (binární protokol, nízká režie)
- Podpora potvrzení o doručení a historie zpráv
- Mechanismy autentizace a zabezpečení integrované se sítěmi operátorů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture

---

📖 **Anglický originál a plná specifikace:** [WV na 3GPP Explorer](https://3gpp-explorer.com/glossary/wv/)
