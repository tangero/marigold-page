---
slug: "sacch-c4"
url: "/mobilnisite/slovnik/sacch-c4/"
type: "slovnik"
title: "SACCH/C4 – Slow Associated Control CHannel/SDCCH/4"
date: 2025-01-01
abbr: "SACCH/C4"
fullName: "Slow Associated Control CHannel/SDCCH/4"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sacch-c4/"
summary: "Specifická konfigurace SACCH přidruženého k SDCCH/4 (samostatný vyhrazený řídicí kanál se 4 subkanály). Poskytuje potřebné signalizační spojení pro sestavení hovoru, aktualizaci polohy a SMS na SDCCH"
---

SACCH/C4 je konfigurace pomalého přidruženého řídicího kanálu (Slow Associated Control Channel) pro SDCCH/4, která poskytuje signalizační spojení pro sestavení hovoru, aktualizace polohy a SMS a zároveň přenáší měřicí a řídicí data.

## Popis

[SACCH](/mobilnisite/slovnik/sacch/)/C4 označuje pomalý přidružený řídicí kanál (Slow Associated Control Channel), který je specificky přidružen ke konfiguraci [SDCCH](/mobilnisite/slovnik/sdcch/)/4 v sítích GSM. SDCCH (Standalone Dedicated Control Channel) je vyhrazený signalizační kanál používaný pro procedury jako sestavení hovoru, aktualizace polohy (location area updating) a přenos [SMS](/mobilnisite/slovnik/sms/), které probíhají před přidělením kanálu pro přenos hovoru (Traffic Channel, [TCH](/mobilnisite/slovnik/tch/)) nebo když je vyžadována pouze signalizace. Část '/4' označuje specifickou multiplexní konfiguraci, kde jsou čtyři nezávislé SDCCH subkanály mapovány na jeden fyzický kanál (jeden časový slot). SACCH/C4 je přidružený řídicí kanál spárovaný s touto konfigurací SDCCH/4.

Z architektonického hlediska, když je mobilní stanici přidělen SDCCH subkanál (např. pro provedení aktualizace polohy), je jí současně přidělen odpovídající zdroj SACCH. SACCH/C4 je časově multiplexován se subkanály SDCCH/4 v rámci specifické 51-rámcové multirámcové struktury používané pro řídicí kanály. V této struktuře jsou určité rámce vyhrazeny pro SACCH. Tím je během transakce na SDCCH zajištěna nepřetržitá, byť pomalá, obousměrná signalizační cesta mezi [MS](/mobilnisite/slovnik/ms/) a [BTS](/mobilnisite/slovnik/bts/). SACCH/C4 přenáší stejný typ signalizačních zpráv vrstvy 3 jako SACCH přidružený k TCH, ale jeho role je klíčová během těchto předvolacích nebo nevolacích signalizačních fází.

Jeho funkce je nedílnou součástí stability přístupu k síti. Zatímco mobilní stanice používá SDCCH subkanál pro signalizaci (např. odesílání [CM](/mobilnisite/slovnik/cm/) SERVICE REQUEST), je současně aktivní přidružený SACCH/C4. Mobilní stanice používá tento SACCH k odesílání měřicích reportů do sítě, stejně jako by to dělala během hovoru. To umožňuje síti monitorovat rádiové podmínky i během sestavování hovoru. Pokud se signál výrazně zhorší, síť může proceduru přerušit nebo podniknout nápravná opatření. Síť také používá SACCH/C4 k odesílání systémových informací a příkazů pro řízení výkonu k mobilní stanici. Tím je zajištěno správné nastavení vysílání mobilní stanice a že má potřebné parametry buňky, což činí signalizační výměnu na SDCCH spolehlivější a připravuje mobilní stanici na případný následný přechod na TCH.

## K čemu slouží

Účelem [SACCH](/mobilnisite/slovnik/sacch/)/C4 je poskytnout potřebný dohled a řízení rádiového spoje pro signalizační transakce probíhající na SDCCH/4. Před vznikem GSM signalizace během sestavování hovoru často postrádala vyhrazený přidružený řídicí mechanismus, což činilo procedury zranitelnými vůči selháním způsobeným měnícími se rádiovými podmínkami. SACCH/C4 tento problém řeší tím, že zajišťuje, aby i během krátkých signalizačních výměn (jako je autentizace nebo sestavení hovoru) síť udržovala řídicí kanál pro sledování kvality spoje a správu rádiového připojení.

To je obzvláště důležité, protože procedury na SDCCH jsou kritickými předstupni pro sestavení hovoru nebo aktualizace polohy. Selhání způsobené špatnými rádiovými podmínkami by vedlo ke špatnému uživatelskému zážitku (nezdařené pokusy o hovor, nedoručené SMS). SACCH/C4 umožňuje síti přijímat měřicí reporty během těchto procedur, což jí umožňuje v případě potřeby nařídit změnu buňky (cell reselection) nebo zajistit, že mobilní stanice používá správný výkon a časování. V podstatě rozšiřuje robustní principy správy spojení z fáze přenosu hovoru (TCH+SACCH) do fáze vyhrazené signalizace, čímž zajišťuje celkovou spolehlivost a efektivitu sítě od okamžiku, kdy se mobilní stanice pokusí o přístup k síti.

## Klíčové vlastnosti

- Specificky přidružen ke konfiguraci signalizačního kanálu SDCCH/4
- Funguje v rámci 51-rámcové multirámcové struktury řídicích kanálů
- Poskytuje nepřetržitou signalizaci během sestavování hovoru, SMS a aktualizací polohy
- Přenáší měřicí reporty do sítě během používání SDCCH
- Přenáší síťové příkazy pro řízení výkonu a systémové informace
- Zvyšuje spolehlivost počátečního přístupu k síti a signalizačních procedur

## Související pojmy

- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [TCH – Traffic Channel](/mobilnisite/slovnik/tch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [SACCH/C4 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sacch-c4/)
