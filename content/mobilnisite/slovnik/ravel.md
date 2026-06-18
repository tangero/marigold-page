---
slug: "ravel"
url: "/mobilnisite/slovnik/ravel/"
type: "slovnik"
title: "RAVEL – Roaming Architecture for VoicE over IMS with Local breakout"
date: 2025-01-01
abbr: "RAVEL"
fullName: "Roaming Architecture for VoicE over IMS with Local breakout"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ravel/"
summary: "Architektonický rámec 3GPP pro poskytování hlasových služeb založených na IMS (VoLTE, VoNR) a dalších služeb roamujícím účastníkům s využitím lokálního průniku (local breakout). Směruje uživatelskou r"
---

RAVEL je architektonický rámec 3GPP pro poskytování hlasových a dalších služeb založených na IMS roamujícím účastníkům směrováním provozu lokálně prostřednictvím navštívené sítě za účelem snížení latence a nákladů.

## Popis

RAVEL (Roaming Architecture for VoicE over IMS with Local breakout) je standardizovaná architektura definovaná 3GPP pro umožnění služeb IP Multimedia Subsystem (IMS), především hlasové a videotelefonie, pro roamující uživatele. Konkrétně využívá pro uživatelskou rovinu model lokálního průniku (Local Breakout, [LBO](/mobilnisite/slovnik/lbo/)). Při tradičním roamingu se směrováním do domácí sítě je veškerý provoz uživatelské roviny (hlasové pakety) tunelován zpět do brány Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) domácí sítě, než dosáhne jádra IMS nebo internetu. RAVEL to mění tím, že ukotvuje uživatelskou rovinu v PGW navštívené sítě (vPLMN PGW). To znamená, že mediální pakety pro hovor mezi dvěma roamujícími uživateli ve stejné navštívené zemi mohou proudit přímo mezi nimi bez průchodu jejich příslušnými domácími sítěmi.

Architektura zahrnuje několik klíčových síťových funkcí. V navštívené síti uživatelskou rovinu zpracovávají Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a [PDN](/mobilnisite/slovnik/pdn/) Gateway (PGW). Navštívená síť také hostí Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), což je první kontaktní bod UE pro signalizaci IMS. P-CSCF může být umístěna v navštívené síti (Visited P-CSCF) nebo zůstat v domácí síti. Pro RAVEL s plným lokálním průnikem se používá Visited P-CSCF. Signalizace IMS je však typicky stále směrována do jádra IMS domácí sítě (např. domácí [S-CSCF](/mobilnisite/slovnik/s-cscf/)) pro řízení služeb a dotazování na profil účastníka. Tím vzniká rozdělení: signalizace řídicí roviny jde do domácí sítě, zatímco přenosová cesta medií uživatelské roviny je zřízena lokálně.

Toto oddělení je řízeno pomocí architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Funkce Policy and Charging Rules Function navštívené sítě (vPCRF) komunikuje přes roamingové rozhraní S9 s domácí [PCRF](/mobilnisite/slovnik/pcrf/) (hPCRF), aby získala pravidla politiky pro účastníka. Tato pravidla jsou pak vynucována v navštívené PGW funkcí Policy and Charging Enforcement Function (PCEF). To zajišťuje, že domácí operátor si zachovává kontrolu nad kvalitou služeb a účtováním, i když je uživatelská rovina přerušena lokálně. RAVEL je zásadní pro efektivní roaming VoLTE/VoNR, protože minimalizuje latenci (kritickou pro kvalitu hlasu), snižuje náklady na přenosovou kapacitu na propojích mezi operátory a umožňuje optimální směrování médií, zejména pro lokalizované hovory a přístup ke službám navštívené sítě.

## K čemu slouží

RAVEL byl vyvinut k řešení technických a ekonomických neefektivit roamingu se směrováním do domácí sítě pro služby komunikace v reálném čase založené na IMS, jako je VoLTE. Rané architektury roamingu IMS se často spoléhaly na směrování do domácí sítě, kde byl veškerý provoz veden přes síť domácího operátora. Tento model přinášel významnou latenci (kvůli 'trombónovému' efektu paketů putujících na velké vzdálenosti), zvyšoval přenosové náklady pro oba operátory a vytvářel suboptimální přenosové cesty médií (např. hovor mezi dvěma uživateli roamujícími ve stejném městě by měl média směrovaná přes jejich příslušné domovské země). Tyto problémy byly škodlivé pro uživatelský zážitek z hlasových a video služeb, které jsou vysoce citlivé na zpoždění a ztrátu paketů.

Motivací pro RAVEL bylo umožnit roamujícím účastníkům 'lokální zážitek', odpovídající kvalitě a efektivitě domácí služby. Přijetím lokálního průniku RAVEL řeší omezení modelu se směrováním do domácí sítě. Umožňuje navštíveným operátorům využít jejich vlastní lokální síťové zdroje a partnerské dohody pro doručování médií. To je obzvláště důležité pro komerční úspěch roamingu VoLTE/VoNR, protože to operátorům umožňuje nabízet služby nákladově efektivně a zajišťuje vysokou kvalitu pro koncové uživatele. Vývoj RAVEL ve verzi 11 byl součástí širšího úsilí učinit hlas založený na IMS životaschopnou a lepší náhradou za circuit-switched fallback (CSFB) během roamingu, čímž se připravila cesta pro všudypřítomný HD hlas a budoucí komunikační služby.

## Klíčové vlastnosti

- Ukotvení uživatelské roviny lokálního průniku (LBO) v PGW navštívené PLMN
- Oddělení řídicí (směrované do domácí sítě) a uživatelské (lokální) roviny
- Využívá Visited P-CSCF pro přístup k IMS
- Využívá rozhraní S9 pro roaming PCC mezi vPCRF a hPCRF
- Umožňuje optimální směrování médií a sníženou latenci pro roamující hovory
- Podporuje VoLTE, VoNR, ViLTE a další multimediální služby IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [RAVEL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ravel/)
